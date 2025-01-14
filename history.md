---
title: History
layout: default
sort_index: 2
---

<div id="history-container"></div>

<button onclick="reset()">Reset</button>


<script>
let h;

function reset() {
	h.resetHistory();
	main();
}

function main(hist) {
	h = hist;
	let container = document.getElementById('history-container');
	container.innerHTML = '';

	Object.entries(h.iterPerDay()).forEach(([date, hist]) => {

		let content = hist.map((e) => `<li>${h.data[e['prg']]['name']} ${e['set']}</li>`).join('\n')

		container.innerHTML += `<h2>${date}</h2>` + "<ul>" + content + "</ul>";
	});
}


function init() {
	const level_reg = /\d+/;
	fetch("/assets/data.json")
	.then(response => response.json())
	.then(json => {
		data = json.reduce((acc, e) => {
			if (e['level']) {
				e['level'] = e['level'].map(l => {
					let [times, reps] = l.match(/\d+/g).map(n => parseInt(n, 10));
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
		let hist = new History();
		hist.data = data;
		main(hist);
	});
}
document.body.onload = init
</script>