SELECT
	e.event_id,
	e.title,
	ROUND(
		AVG(
			TIMESTAMPDIFF(
				MINUTE,
				s.start_time,
				s.end_time
			)
		),
		2
	) AS avg_duration_minutes
FROM Events e
JOIN Sessions s
	ON e.event_id = s.event_id
GROUP BY e.event_id, e.title;

Example

If an event contains:

Session 1 = 60 mins
Session 2 = 75 mins

Average:

67.5 mins
