## Orientation

The actual hybrid calisthenics app is great because of its content and design: it is straight to the point, no major gamification, and it is very encouraging !
The major flaw is that the logging mechanism is buggy and isn't shared between routine and movement library. Also i cannot track what I did last time. Also the loading time between each page is too long.

I want to make a copy of the app with a non buggy logging mechanism and a short loading time.

I would like to add a minimal history to keep track of my progress. This must be very minimal in order to keep the app straight to the points, which is: having info on the movements and info about the routine each day.
Looking at the [community ressources](https://www.hybridcalisthenics.com/community-resources), it seem common to track the history offline (which is a good thing imho). Maybe adding a history is overkill, just fixing the logging system is enough.

```bash
cd src
scrapy runspider hybrid_calisthenics.py -O ../assets/data.json
```

## Vues

Movement Library -> same as app
	Movement Page -> same as app
		Progression Page -> same as app
Home Screen
	- Streak
	- What to do today
History -> New page
Profile
Routine

## User Stories:

    User Story: learn about exercices:
    I want to know how to perform specific exercises from HybridCalisthenics.

  	User Story: keep track of workout sessions
  	I want to be able to know which exercices (sets and reps) I did on a specific day.

  	User Story: routine recommandation
  	I want a routine to be recommanded to me based on my progress.


## Todo

[x] Add urls in scraper (to have a unique ID per progression) and unify overview and progression info.
[x] Refactor collection at progression level instead of movement. (add a movement attribute).
[x] Create "Movement Library" page
[x] Create "Movement" layout
[x] Think about how to log sets (add 3 text box next to progression in movement and progression)
[x] Create "Progression" layout
[x] Map video urls from `shinosteph/calisthenics-routine`
[x] Create the `level` variable in JS
[x] Create the `movemement` variable in JS
[x] Display the next level to attain (given the history)
[x] Generer automatiquement la routine du jour
[x] Display the last logged set or the first level

[ ] Think of a workout page (with a timer etc...)
	- it should have a way to validate 1 set, then wait 3 minutes
	- it should display the video
	- maybe just add a logging interface to the progression page (but then it doesn't feel like a Routine as it feels in the app)
	- Now:
	1. Home -> Let's Go (exercices)
	2. Workout Detail -> Let's Go (Repetition + Rest + Cute speech)
	3. Movement 1 -> Log Sets (progression page with an Arrow)
		- Useless
	4. Exercice -> Save Hold (Video, Movement 1 of 2, Set 1 - 15 +, Cute speech, Level, Set 1)
	5. Wait -> X (optionnal + cute speech)
	6. Go to 4
[ ] Load / save history (for inter device)
	- save button: creates a text area with the json inside and a button to copy to clipboard (in pretty print so people can easily edit)
	- load button: creates a text area to paste in and a validation button.
		- the validation should trigger a message stating the total workouts and make understand that it will overwrite the current history
[ ] Allow to change routine (see the routine variable)
[ ] Allow to edit history

- Think about how to display history (per movement, per progression, dedicated tab, using a calendar)