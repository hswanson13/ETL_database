--
-- PostgreSQL database dump
--

-- Dumped from database version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: assembly; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assembly (
    id integer NOT NULL,
    user_id integer,
    module_id integer NOT NULL,
    stage_id integer NOT NULL,
    location character varying(50),
    data character varying(50),
    "time" timestamp without time zone DEFAULT now(),
    component_id character varying
);


ALTER TABLE public.assembly OWNER TO postgres;

--
-- Name: assembly_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.assembly ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.assembly_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: assembly_lookup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assembly_lookup (
    id integer NOT NULL,
    stage_name character varying(50) NOT NULL
);


ALTER TABLE public.assembly_lookup OWNER TO postgres;

--
-- Name: assembly_lookup_stage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.assembly_lookup ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.assembly_lookup_stage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: component; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.component (
    id integer NOT NULL,
    module_id integer NOT NULL,
    location character varying(50),
    component_type_id integer,
    component_serial_number character varying NOT NULL
);


ALTER TABLE public.component OWNER TO postgres;

--
-- Name: component_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.component ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.component_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: component_type_lookup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.component_type_lookup (
    id integer NOT NULL,
    component_name character varying(50) NOT NULL
);


ALTER TABLE public.component_type_lookup OWNER TO postgres;

--
-- Name: component_type_lookup_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.component_type_lookup ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.component_type_lookup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying NOT NULL,
    affiliation character varying(50),
    created_at timestamp without time zone DEFAULT now(),
    active_user boolean
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: etl_database_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.etl_database_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.etl_database_users_id_seq OWNER TO postgres;

--
-- Name: etl_database_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.etl_database_users_id_seq OWNED BY public."user".id;


--
-- Name: module; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.module (
    id integer NOT NULL,
    current_location character varying(50),
    module_serial_number character varying NOT NULL
);


ALTER TABLE public.module OWNER TO postgres;

--
-- Name: module_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.module ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.module_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test (
    id integer NOT NULL,
    user_id integer,
    module_id integer,
    component_id integer,
    test_type_id integer NOT NULL,
    location character varying(50),
    data character varying,
    "time" timestamp without time zone DEFAULT now()
);


ALTER TABLE public.test OWNER TO postgres;

--
-- Name: test_lookup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_lookup (
    id integer NOT NULL,
    test_name character varying(150) NOT NULL
);


ALTER TABLE public.test_lookup OWNER TO postgres;

--
-- Name: test_lookup_test_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.test_lookup ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.test_lookup_test_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.etl_database_users_id_seq'::regclass);


--
-- Data for Name: assembly; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assembly (id, user_id, module_id, stage_id, location, data, "time", component_id) FROM stdin;
1	2	1	1	Boston	its on	2023-08-18 17:58:09.258658	
2	2	1	2	Boston	ETROC postion data	2023-08-18 17:59:40.626958	1
3	2	1	2	Boston	LGAD position data	2023-08-18 18:00:34.669483	2
\.


--
-- Data for Name: assembly_lookup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assembly_lookup (id, stage_name) FROM stdin;
1	film
2	pick and place
3	cure
4	wirebond
\.


--
-- Data for Name: component; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.component (id, module_id, location, component_type_id, component_serial_number) FROM stdin;
1	1	Boston	1	c1
2	1	Boston	2	l1
\.


--
-- Data for Name: component_type_lookup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.component_type_lookup (id, component_name) FROM stdin;
1	ETROC
2	LGAD
\.


--
-- Data for Name: module; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.module (id, current_location, module_serial_number) FROM stdin;
1	Boston	m1
2	Nebraska	m2
3	Boston	m3
\.


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test (id, user_id, module_id, component_id, test_type_id, location, data, "time") FROM stdin;
\.


--
-- Data for Name: test_lookup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_lookup (id, test_name) FROM stdin;
1	IV
2	Threshold
3	Pixel_Alive
4	Temperature
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, email, password, affiliation, created_at, active_user) FROM stdin;
4	caleb	c@bu.edu	ps4	Boston	2023-08-18 11:45:02.561261	t
2	hayden	h@bu.edu	ps1	Boston	2023-08-18 11:18:21.466897	t
\.


--
-- Name: assembly_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.assembly_id_seq', 3, true);


--
-- Name: assembly_lookup_stage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.assembly_lookup_stage_id_seq', 4, true);


--
-- Name: component_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.component_id_seq', 2, true);


--
-- Name: component_type_lookup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.component_type_lookup_id_seq', 2, true);


--
-- Name: etl_database_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.etl_database_users_id_seq', 4, true);


--
-- Name: module_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.module_id_seq', 3, true);


--
-- Name: test_lookup_test_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_lookup_test_type_id_seq', 4, true);


--
-- Name: assembly_lookup Assembly_Lookup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly_lookup
    ADD CONSTRAINT "Assembly_Lookup_pkey" PRIMARY KEY (id);


--
-- Name: assembly Assembly_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly
    ADD CONSTRAINT "Assembly_pkey" PRIMARY KEY (id);


--
-- Name: component_type_lookup Component_Type_Lookup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_type_lookup
    ADD CONSTRAINT "Component_Type_Lookup_pkey" PRIMARY KEY (id);


--
-- Name: component Components_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT "Components_pkey" PRIMARY KEY (id);


--
-- Name: module Modules_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.module
    ADD CONSTRAINT "Modules_pkey" PRIMARY KEY (id);


--
-- Name: test_lookup Test_Lookup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_lookup
    ADD CONSTRAINT "Test_Lookup_pkey" PRIMARY KEY (id);


--
-- Name: test Test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "Test_pkey" PRIMARY KEY (id);


--
-- Name: assembly_lookup assembly_lookup_stage_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly_lookup
    ADD CONSTRAINT assembly_lookup_stage_name_key UNIQUE (stage_name);


--
-- Name: component_type_lookup component_type_lookup_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_type_lookup
    ADD CONSTRAINT component_type_lookup_name_key UNIQUE (component_name);


--
-- Name: test_lookup test_lookup_test_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_lookup
    ADD CONSTRAINT test_lookup_test_name_key UNIQUE (test_name);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: user users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: assembly Assembly_module_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly
    ADD CONSTRAINT "Assembly_module_id_fkey" FOREIGN KEY (module_id) REFERENCES public.module(id);


--
-- Name: assembly Assembly_stage_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly
    ADD CONSTRAINT "Assembly_stage_id_fkey" FOREIGN KEY (stage_id) REFERENCES public.assembly_lookup(id);


--
-- Name: assembly Assembly_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assembly
    ADD CONSTRAINT "Assembly_user_id_fkey" FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: component Components_component_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT "Components_component_type_id_fkey" FOREIGN KEY (component_type_id) REFERENCES public.component_type_lookup(id);


--
-- Name: component Components_module_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT "Components_module_id_fkey" FOREIGN KEY (module_id) REFERENCES public.module(id);


--
-- Name: test Test_component_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "Test_component_id_fkey" FOREIGN KEY (component_id) REFERENCES public.component(id);


--
-- Name: test Test_module_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "Test_module_id_fkey" FOREIGN KEY (module_id) REFERENCES public.module(id);


--
-- Name: test Test_test_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "Test_test_type_id_fkey" FOREIGN KEY (test_type_id) REFERENCES public.test_lookup(id);


--
-- Name: test Test_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "Test_user_id_fkey" FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

