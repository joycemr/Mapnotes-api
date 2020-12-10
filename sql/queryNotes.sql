-- select * from notes;

-- select * from note_features;
select id, notes_id, ST_AsText(geometry) from note_features;

-- delete from note_features;