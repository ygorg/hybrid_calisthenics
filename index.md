---
title: Home
layout: default
---

<link rel="stylesheet" type="text/css" href="assets/progression_card.css">

<style>
.streak-week .streak-day {
	background-color: pink;
	border-radius: 100%;
	text-align: center;
	width: 30px;
	height: 30px;
	margin: 3px;
	float: left;
}
</style>

<h1>Greetings, friend</h1>

<span>Hey friend it looks like you have a streak going, keep it up!</span>

<div class="streak-container">
	<div class="streak-week">
	{% for num in (1...7) %}
		<div class="streak-day">{{num}}</div>
	{% endfor %}
	</div>
	<div>
		<p>
			<span>5</span>
			<span>Day Activity Streak</span>
		</p>
		<p>
			<span>22</span>
			<span>Total Workouts</span>
		</p>
	</div>
</div>

<h2>Start Your New Routine</h2>

<div>
	<h2>January 8th</h2>
	{% assign p = site.progression[0] %}
	{% include progression_card.html %}
	{% assign p = site.progression[3] %}
	{% include progression_card.html %}
</div>