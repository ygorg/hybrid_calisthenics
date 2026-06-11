function load_movement_data(callback) {
	const level_reg = /\d+/g;
	fetch("/assets/data.json")
	.then(response => response.json())
	.then(json => {
		data = json.reduce((acc, e) => {
			if (e['level']) {
				e['level'] = e['level'].map(l => {
					let [times, reps] = l.match(level_reg).map(n => parseInt(n, 10));
					if (reps === undefined) {
						// If the level sentences looks like "Hold for 6 seconds"
						reps = times;
						times = 1;
					}
					return [...Array(times)].map(_ => reps);
				})
			}
			if (e['prg_idx']) {
				acc[e['prg_idx']] = e;
			} else {
				acc[e['mvt_idx']] = e;
			}
			return acc;
		}, {});
		// Because we use fetch we cannot simply return the object !
		callback(data);
	});
}