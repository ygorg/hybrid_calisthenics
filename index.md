---
title: Home
layout: default
sort_index: 0
---

<h1>Greetings, friend</h1>

<span>Hey friend it looks like you have a streak going, keep it up!</span>
<!--span>Let's Get Moving !</span-->

<div class="streak-container">
	<div class="streak-week">
	{% assign arr = "S,M,T,W,T,F,S" | split: ',' %}
	{% for day in arr %}
		<div class="streak-day">{{day}}</div>
	{% endfor %}
	</div>
	<div class="streak-info-container">
		<div class="streak-info">
			<p class="streak-nb" id="streak-count">5</p>
			<p class="streak-legend">Day Activity Streak</p>
		</div>
		<div class="streak-info">
			<p class="streak-nb" id="workout-count">22</p>
			<p class="streak-legend">Total Workouts</p>
		</div>
	</div>
</div>

<h2>Start Your New Routine</h2>

<div class="routine-container">
	<h2 style="margin-top:0px">January 8th</h2>
	<div class="progression-container"></div>
</div>

<script type="text/javascript" src="{{ "assets/utils.js" | relative_url }}"></script>

<script type="text/javascript" src="{{ "assets/movement_card.js" | relative_url }}"></script>

<script type="text/javascript">
let h;

const routines = {
	'hybrid_routine2.0': [
		['pushups', 'legraises'],
		['pullups', 'squats'],
		['twists', 'bridges'],
		['pushups', 'legraises'],
		['pullups', 'squats'],
		['twists', 'bridges'],
		'rest'
	],
	'pure_strength': [
		['pushups', 'legraises', 'squats'],
		['pullups', 'bridges', 'clutchflags'],
		'rest',
		['pushups', 'legraises', 'squats'],
		['pullups', 'bridges', 'clutchflags'],
		['pushups', 'legraises', 'squats', 'pullups', 'twists'],
		'rest',
	],
	'solid_start': [
		['pushups', 'leg raises'],
		'rest',
		['pullups', 'squats'],
		'rest',
		['bridges'],
		'rest',
		'rest',
	],
	'work_week': [
		['pullups'],
		['bridges'],
		['pushups'],
		['leg raises'],
		['squats'],
		'rest',
		'rest',
	],
};

function nextRoutine() {
	const current_routine = "hybrid_routine2.0";
	const day = new Date().getDay();
	return routines[current_routine][day];
}

function init() {
    load_movement_data(data => {
        let hist = new History();
        hist.data = data;
        main(hist);
    });
}

function main(hist) {
	h = hist;

	const date = new Date();
	[...document.getElementsByClassName('streak-day')].forEach((e, i) => {
		if (i <= date.getDay()) {e.classList.add('past')}
		if (h.getDay(date.getFullYear(), date.getMonth()+1, date.getDate() - date.getDay() + i)) {e.classList.add('done')}
	});

	document.getElementById('streak-count').innerHTML = h.streakCount();
	document.getElementById('workout-count').innerHTML = Object.keys(h.iterPerDay()).length;
	
	let month = date.toLocaleString('en-US', { month: 'long' });
	month = month[0].toUpperCase() + month.substring(1);
	//@ from https://stackoverflow.com/a/39466341
	function nth(n){return n + ["st","nd","rd"][((n+90)%100-10)%10-1]||n+"th"}
	document.querySelector('.routine-container h2').innerHTML = `${month} ${nth(date.getDate())}`;

    let container = document.getElementsByClassName('progression-container')[0];
    let nextMovements = nextRoutine();
    if (nextMovements === 'rest') {
    	container.innerHTML += "Today is rest day ! Come back tomorrow.";
    } else {
		nextMovements.map(mvt => createProgCard(
				h.currentProgression(h.data[mvt]['progression']),
				h.data
			)
		).forEach((html) => {
			container.innerHTML += html;
		});
	}

	/*[...document.getElementsByClassName('progression-card')].forEach(
        e => e.getElementsByTagName('button')[0].addEventListener('click', logset)
    );*/
}

document.body.onload = init
</script>