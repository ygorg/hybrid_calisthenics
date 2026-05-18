const history = {
  //"full-bridges": [{"date": "2025-01-01T11:05", "set": [10, 10, 10]}]
};

class History {
  constructor() {
    // A history is a map {progression: [{date, set}]}
    this.history = {};
    // The data about progression (only used in log2level)
    this.data = null;
    this.loadHistory();
    // The maximum number of level in a progression.
    this.MAX_LEVEL = 3;
  }

  loadHistory() {
    const json = localStorage.getItem('history');
    if (!json) {
      this.history = {};
    } else {
      this.history = JSON.parse(json);  
    }
  }

  saveHistory() {
    localStorage.setItem(
      "history",
      JSON.stringify(this.history)
    );
  }

  resetHistory() {
    localStorage.removeItem('history');
    this.loadHistory();
  }

  logSet(prg_idx, set, date) {
    /**
     * Given a progression, a repetition set and a date, add it to the history.
     */
    if (!this.history[prg_idx]) {
      this.history[prg_idx] = [];
    }
    if (!date) {
      date = new Date().toISOString()
    }
    //Prepend new set to progression history.
    this.history[prg_idx].unshift({"date": date, "set": set});
    this.saveHistory();
  }

  attempted(progression) {
    /**
     * Returns True if the progression was attempted
     */
    return progression in this.history;
  }

  lastSet(progression) {
    /**
     * Returns the last logged set for the given progression
     */
    return this.history[progression][0];
  }

  streakCount() {
    /**
     * Count the number of days from today with at least a saved set.
     * TODO: how to include rest days ?
     */
    let i = 0;
    let date = new Date();
    let workDate = Object.keys(this.iterPerDay());
    while (workDate.includes(date.toISOString().slice(0,10))) {
      i += 1;
      date.setDate(date.getDate() - 1);
    }
    return i;
  }

  log2level(progression, log) {
    /**
     * Given a progression and a logged set, compute which level was achieved.
     */
    // for each level (starting with the highest)
    for (let i = this.data[progression]['level'].length - 1; i >= 0; i--) {
      const sets = this.data[progression]['level'][i];
      // has the log enough sets? and are all the sets better or equal to the current level?
      if (log.length >= sets.length && sets.every((value, index) => log[index] >= value)) {
        return i + 1;
      }
    }
    return 0;
  }

  currentLevel(progression) {
    /**
     * Returns the level of the progression based on previously logged sets.
     */
    // TODO add an option to search only the newer X months

    let maxLevel = 0;

    // For every logged set of the progression
    for (let h of this.history[progression] || []) {
      // find the maximum level achieved
      const level = this.log2level(progression, h['set']);
      if (maxLevel < level) {
        maxLevel = level;
      }

      if (maxLevel === this.MAX_LEVEL) {
        // If we found the maximum level then no need to check the rest
        return maxLevel;
      }
    }

    return maxLevel;
  }

  currentProgression(movement) {
    /**
     * Returns the next progression for a given movement.
     */
    /*
    //V1 : smallest progression not having a level 3; does not account for skipping progression
    for (let progName of movement) {
      // movement is sorted by increasing progression
      if (this.currentLevel(progName) !== this.MAX_LEVEL) {
        return progName;
      }
      return movement.at(-1);
    }*/
    // V2: last attempted progression if level != 3 else last + 1 or first progression
    for (let i = movement.length - 1; i >= 0; i--) {
      const progName = movement[i];
      // movement is sorted by increasing progression so we reverse it
      let level = this.currentLevel(progName);
      console.log(i, level);
      if (level > 0 && level < this.MAX_LEVEL) {
        return progName;
      } else if (level > 0 && level == this.MAX_LEVEL) {
        return movement[Math.min(i+1, movement.length-1)];
      }
    }
    return movement.at(0)
  }

  getDay(year, month, day) {
    /**
     * Return the reps of a given day.
     */
    month = String(month).padStart(2, '0'); // '09'
    day = String(day).padStart(2, '0'); // '09'
    return this.iterPerDay()[`${year}-${month}-${day}`];
  }

  iterPerDay() {
    /**
     * Return a copy of the history as a map {day: [date, progression, set]}
     */
    // Create an array [{date, progression, reps}]
    let arr = [];
    for (let key in this.history) {
      let mov_hist = this.history[key];
      mov_hist.forEach((e) => e['prg'] = key);
      arr = arr.concat(mov_hist)
    };

    var groupBy = function(xs, key) {
      return xs.reduce(function(rv, x) {
        (rv[key(x)] = rv[key(x)] || []).push(x);
        return rv;
      }, {});
    };

    // Group the array by date
    let groupedHist = groupBy(arr, (e) => new Date(e['date'].slice(0,10)));

    // Modify the date to only keep YYMMDD and sort
    const altObj = Object.fromEntries(
      Object.entries(groupedHist).map(([key, value]) => 
        // Modify key here
        [value[0]['date'].slice(0,10), value]
      ).sort().reverse()
    )
    return altObj;
  }
}