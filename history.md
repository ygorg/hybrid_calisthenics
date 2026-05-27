---
title: History
layout: default
sort_index: 2
---

<div id="history-container"></div>

<button onclick="reset()">Reset</button>

<script type="text/javascript" src="/assets/utils.js"></script>
<script type="text/javascript">
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
		let content = hist.map((e) => `<li><a href="progression/${e['prg']}.html">${h.data[e['prg']]['name']}</a> : ${e['set']}</li>`).join('\n')

		container.innerHTML += `<h2>${date}</h2>` + "<ul>" + content + "</ul>";
	});
}

function init() {
    load_movement_data(data => {
        let hist = new History();
        hist.data = data;
        main(hist);
    });
}

document.body.onload = init
</script>