CREATE TABLE public.notes
(
    id integer NOT NULL,
    body text,
    title varchar(255),
    CONSTRAINT notes_pkey PRIMARY KEY (id)
);

CREATE TABLE public.note_features
(
    id integer NOT NULL,
    geometry geometry,
    notes_id integer NOT NULL,
    CONSTRAINT note_features_pkey PRIMARY KEY (id),
    CONSTRAINT note_fk FOREIGN KEY (notes_id)
        REFERENCES public.notes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE SEQUENCE public.note_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE SEQUENCE public.note_features_surrogate_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;
