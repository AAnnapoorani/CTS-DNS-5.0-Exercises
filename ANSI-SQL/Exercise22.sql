SELECT
	user_id,
	event_id,
	COUNT(*) AS registration_count
FROM Registrations
GROUP BY user_id, event_id
HAVING COUNT(*) > 1;

Expected Result

If no duplicate registrations exist:

Empty Set
