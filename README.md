## Orientation

The actual hybrid calisthenics app is great because of its content and design: it is straight to the point, no major gamification, and it is very encouraging !
The major flaw is that the logging mechanism is buggy and isn't shared between routine and movement library. Also i cannot track what I did last time. Also the loading time between each page is too long.

I want to make a copy of the app with a non buggy logging mechanism and a short loading time.

I would like to add a minimal history to keep track of my progress. This must be very minimal in order to keep the app straight to the points, which is: having info on the movements and info about the routine each day.
Looking at the [community ressources](https://www.hybridcalisthenics.com/community-resources), it seem common to track the history offline (which is a good thing imho). Maybe adding a history is overkill, just fixing the logging system is enough.

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
[ ] Display the next level to attain (given the history)
[ ] Map video urls from `shinosteph/calisthenics-routine`


[ ] Generer automatiquement la routine du jour
- For each movement display next target
- Think about how to display history (per movement, per progression, dedicated tab)
- Import / Export history