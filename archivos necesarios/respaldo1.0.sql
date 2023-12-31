PGDMP                         {            pab_db    15.4    15.4 K    ]           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ^           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            _           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            `           1262    16923    pab_db    DATABASE     }   CREATE DATABASE pab_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';
    DROP DATABASE pab_db;
                postgres    false            �            1259    16924    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    16988    asigna    TABLE     �   CREATE TABLE public.asigna (
    cod_asignar integer NOT NULL,
    ced_estudiante integer NOT NULL,
    cedula_prof integer NOT NULL,
    cod_grado_seccion integer NOT NULL,
    cod_materia character varying(10) NOT NULL
);
    DROP TABLE public.asigna;
       public         heap    postgres    false            �            1259    17013    cursa    TABLE     �   CREATE TABLE public.cursa (
    cod_cursa integer NOT NULL,
    cedula_estudiante integer NOT NULL,
    cod_materia character varying(10) NOT NULL
);
    DROP TABLE public.cursa;
       public         heap    postgres    false            �            1259    16960 
   estudiante    TABLE     F  CREATE TABLE public.estudiante (
    cedula integer NOT NULL,
    responsable character varying(60) NOT NULL,
    tipo_inscrip character varying(30) NOT NULL,
    antecedente_escolar character varying(30) NOT NULL,
    nombres character varying(60) NOT NULL,
    apellidos character varying(60) NOT NULL,
    genero character varying(15) NOT NULL,
    nacionalidad character varying(15) NOT NULL,
    fecha_naci date NOT NULL,
    parto character varying(200) NOT NULL,
    edad integer NOT NULL,
    lateralidad character varying(30) NOT NULL,
    lugar_naci character varying(200) NOT NULL,
    peso double precision NOT NULL,
    estatura double precision NOT NULL,
    hermanos character varying(20) NOT NULL,
    hermanos_inst character varying(20) NOT NULL,
    talla_camisa character varying(10) NOT NULL,
    talla_pantalon character varying(10) NOT NULL,
    salud character varying(50) NOT NULL,
    covid character varying(20) NOT NULL,
    vacunas_covid character varying(50) NOT NULL,
    atencion_espec character varying(50) NOT NULL,
    email_estud character varying(254) NOT NULL,
    equipo_tecn character varying(50) NOT NULL,
    acceso_inter character varying(200) NOT NULL,
    redes_soc character varying(200) NOT NULL,
    canaima character varying(10) NOT NULL,
    representante_id integer,
    cod_grado_seccion integer
);
    DROP TABLE public.estudiante;
       public         heap    postgres    false            �            1259    16959    estudiante_cedula_seq    SEQUENCE     �   CREATE SEQUENCE public.estudiante_cedula_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.estudiante_cedula_seq;
       public          postgres    false    222            a           0    0    estudiante_cedula_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.estudiante_cedula_seq OWNED BY public.estudiante.cedula;
          public          postgres    false    221            �            1259    17066    grado_seccion    TABLE     �   CREATE TABLE public.grado_seccion (
    cod_grado_seccion integer NOT NULL,
    grado_seccion character varying(50) NOT NULL
);
 !   DROP TABLE public.grado_seccion;
       public         heap    postgres    false            �            1259    17065 #   grado_seccion_cod_grado_seccion_seq    SEQUENCE     �   CREATE SEQUENCE public.grado_seccion_cod_grado_seccion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public.grado_seccion_cod_grado_seccion_seq;
       public          postgres    false    230            b           0    0 #   grado_seccion_cod_grado_seccion_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public.grado_seccion_cod_grado_seccion_seq OWNED BY public.grado_seccion.cod_grado_seccion;
          public          postgres    false    229            �            1259    17028    imparte    TABLE     �   CREATE TABLE public.imparte (
    cod_imparte integer NOT NULL,
    cod_materia character varying(10) NOT NULL,
    cod_grado_seccion integer NOT NULL
);
    DROP TABLE public.imparte;
       public         heap    postgres    false            �            1259    16978    materia    TABLE     �   CREATE TABLE public.materia (
    cod_materia character varying(10) NOT NULL,
    nom_materia character varying(50) NOT NULL,
    cedula_prof integer
);
    DROP TABLE public.materia;
       public         heap    postgres    false            �            1259    17044    nota    TABLE     &  CREATE TABLE public.nota (
    cod_nota integer NOT NULL,
    nota_1er_lapso integer NOT NULL,
    nota_2do_lapso integer NOT NULL,
    nota_3er_lapso integer NOT NULL,
    promedio integer NOT NULL,
    ced_estudiante integer,
    cod_materia character varying(10),
    cedula_prof integer
);
    DROP TABLE public.nota;
       public         heap    postgres    false            �            1259    17043    nota_cod_nota_seq    SEQUENCE     �   CREATE SEQUENCE public.nota_cod_nota_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.nota_cod_nota_seq;
       public          postgres    false    228            c           0    0    nota_cod_nota_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.nota_cod_nota_seq OWNED BY public.nota.cod_nota;
          public          postgres    false    227            �            1259    16937    profesor    TABLE     �   CREATE TABLE public.profesor (
    cedula_prof integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50) NOT NULL
);
    DROP TABLE public.profesor;
       public         heap    postgres    false            �            1259    16936    profesor_cedula_prof_seq    SEQUENCE     �   CREATE SEQUENCE public.profesor_cedula_prof_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.profesor_cedula_prof_seq;
       public          postgres    false    216            d           0    0    profesor_cedula_prof_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.profesor_cedula_prof_seq OWNED BY public.profesor.cedula_prof;
          public          postgres    false    215            �            1259    16944    representante    TABLE     &  CREATE TABLE public.representante (
    nombre character varying(60) NOT NULL,
    apellido character varying(60) NOT NULL,
    nacionalidad character varying(15) NOT NULL,
    cedula integer NOT NULL,
    parentesco character varying(30) NOT NULL,
    lugar_naci character varying(200) NOT NULL,
    telefono bigint NOT NULL,
    telefono_alt bigint NOT NULL,
    profesion character varying(100) NOT NULL,
    telefono_trab bigint NOT NULL,
    direccion_trab character varying(200) NOT NULL,
    vive_chacao character varying(10) NOT NULL,
    direccion_dom character varying(200) NOT NULL,
    estado_viv_infra character varying(100) NOT NULL,
    estado_viv_tipo character varying(100) NOT NULL,
    estado_viv_cond character varying(100) NOT NULL,
    resolucion_0 character varying(150) NOT NULL
);
 !   DROP TABLE public.representante;
       public         heap    postgres    false            �            1259    16943    representante_cedula_seq    SEQUENCE     �   CREATE SEQUENCE public.representante_cedula_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.representante_cedula_seq;
       public          postgres    false    218            e           0    0    representante_cedula_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.representante_cedula_seq OWNED BY public.representante.cedula;
          public          postgres    false    217            �            1259    16953    user    TABLE     
  CREATE TABLE public."user" (
    username integer NOT NULL,
    password character varying(100) NOT NULL,
    names character varying(50) NOT NULL,
    lastnames character varying(50) NOT NULL,
    email character varying(254) NOT NULL,
    phone bigint NOT NULL
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    16952    user_username_seq    SEQUENCE     �   CREATE SEQUENCE public.user_username_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.user_username_seq;
       public          postgres    false    220            f           0    0    user_username_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.user_username_seq OWNED BY public."user".username;
          public          postgres    false    219            �           2604    16963    estudiante cedula    DEFAULT     v   ALTER TABLE ONLY public.estudiante ALTER COLUMN cedula SET DEFAULT nextval('public.estudiante_cedula_seq'::regclass);
 @   ALTER TABLE public.estudiante ALTER COLUMN cedula DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    17069    grado_seccion cod_grado_seccion    DEFAULT     �   ALTER TABLE ONLY public.grado_seccion ALTER COLUMN cod_grado_seccion SET DEFAULT nextval('public.grado_seccion_cod_grado_seccion_seq'::regclass);
 N   ALTER TABLE public.grado_seccion ALTER COLUMN cod_grado_seccion DROP DEFAULT;
       public          postgres    false    230    229    230            �           2604    17047    nota cod_nota    DEFAULT     n   ALTER TABLE ONLY public.nota ALTER COLUMN cod_nota SET DEFAULT nextval('public.nota_cod_nota_seq'::regclass);
 <   ALTER TABLE public.nota ALTER COLUMN cod_nota DROP DEFAULT;
       public          postgres    false    227    228    228            �           2604    16940    profesor cedula_prof    DEFAULT     |   ALTER TABLE ONLY public.profesor ALTER COLUMN cedula_prof SET DEFAULT nextval('public.profesor_cedula_prof_seq'::regclass);
 C   ALTER TABLE public.profesor ALTER COLUMN cedula_prof DROP DEFAULT;
       public          postgres    false    215    216    216            �           2604    16947    representante cedula    DEFAULT     |   ALTER TABLE ONLY public.representante ALTER COLUMN cedula SET DEFAULT nextval('public.representante_cedula_seq'::regclass);
 C   ALTER TABLE public.representante ALTER COLUMN cedula DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    16956    user username    DEFAULT     p   ALTER TABLE ONLY public."user" ALTER COLUMN username SET DEFAULT nextval('public.user_username_seq'::regclass);
 >   ALTER TABLE public."user" ALTER COLUMN username DROP DEFAULT;
       public          postgres    false    219    220    220            J          0    16924    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    214   �d       T          0    16988    asigna 
   TABLE DATA           j   COPY public.asigna (cod_asignar, ced_estudiante, cedula_prof, cod_grado_seccion, cod_materia) FROM stdin;
    public          postgres    false    224   �d       U          0    17013    cursa 
   TABLE DATA           J   COPY public.cursa (cod_cursa, cedula_estudiante, cod_materia) FROM stdin;
    public          postgres    false    225   �d       R          0    16960 
   estudiante 
   TABLE DATA           �  COPY public.estudiante (cedula, responsable, tipo_inscrip, antecedente_escolar, nombres, apellidos, genero, nacionalidad, fecha_naci, parto, edad, lateralidad, lugar_naci, peso, estatura, hermanos, hermanos_inst, talla_camisa, talla_pantalon, salud, covid, vacunas_covid, atencion_espec, email_estud, equipo_tecn, acceso_inter, redes_soc, canaima, representante_id, cod_grado_seccion) FROM stdin;
    public          postgres    false    222   �d       Z          0    17066    grado_seccion 
   TABLE DATA           I   COPY public.grado_seccion (cod_grado_seccion, grado_seccion) FROM stdin;
    public          postgres    false    230   e       V          0    17028    imparte 
   TABLE DATA           N   COPY public.imparte (cod_imparte, cod_materia, cod_grado_seccion) FROM stdin;
    public          postgres    false    226   ne       S          0    16978    materia 
   TABLE DATA           H   COPY public.materia (cod_materia, nom_materia, cedula_prof) FROM stdin;
    public          postgres    false    223   �f       X          0    17044    nota 
   TABLE DATA           �   COPY public.nota (cod_nota, nota_1er_lapso, nota_2do_lapso, nota_3er_lapso, promedio, ced_estudiante, cod_materia, cedula_prof) FROM stdin;
    public          postgres    false    228   mg       L          0    16937    profesor 
   TABLE DATA           A   COPY public.profesor (cedula_prof, nombre, apellido) FROM stdin;
    public          postgres    false    216   �g       N          0    16944    representante 
   TABLE DATA             COPY public.representante (nombre, apellido, nacionalidad, cedula, parentesco, lugar_naci, telefono, telefono_alt, profesion, telefono_trab, direccion_trab, vive_chacao, direccion_dom, estado_viv_infra, estado_viv_tipo, estado_viv_cond, resolucion_0) FROM stdin;
    public          postgres    false    218   �g       P          0    16953    user 
   TABLE DATA           T   COPY public."user" (username, password, names, lastnames, email, phone) FROM stdin;
    public          postgres    false    220   h       g           0    0    estudiante_cedula_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.estudiante_cedula_seq', 1, false);
          public          postgres    false    221            h           0    0 #   grado_seccion_cod_grado_seccion_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public.grado_seccion_cod_grado_seccion_seq', 1, false);
          public          postgres    false    229            i           0    0    nota_cod_nota_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.nota_cod_nota_seq', 1, false);
          public          postgres    false    227            j           0    0    profesor_cedula_prof_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.profesor_cedula_prof_seq', 1, false);
          public          postgres    false    215            k           0    0    representante_cedula_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.representante_cedula_seq', 1, false);
          public          postgres    false    217            l           0    0    user_username_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.user_username_seq', 1, false);
          public          postgres    false    219            �           2606    16928 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    214            �           2606    16992    asigna asigna_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.asigna
    ADD CONSTRAINT asigna_pkey PRIMARY KEY (cod_asignar, ced_estudiante, cedula_prof, cod_grado_seccion, cod_materia);
 <   ALTER TABLE ONLY public.asigna DROP CONSTRAINT asigna_pkey;
       public            postgres    false    224    224    224    224    224            �           2606    17017    cursa cursa_pkey 
   CONSTRAINT     u   ALTER TABLE ONLY public.cursa
    ADD CONSTRAINT cursa_pkey PRIMARY KEY (cod_cursa, cedula_estudiante, cod_materia);
 :   ALTER TABLE ONLY public.cursa DROP CONSTRAINT cursa_pkey;
       public            postgres    false    225    225    225            �           2606    16967    estudiante estudiante_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_pkey PRIMARY KEY (cedula);
 D   ALTER TABLE ONLY public.estudiante DROP CONSTRAINT estudiante_pkey;
       public            postgres    false    222            �           2606    17071     grado_seccion grado_seccion_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.grado_seccion
    ADD CONSTRAINT grado_seccion_pkey PRIMARY KEY (cod_grado_seccion);
 J   ALTER TABLE ONLY public.grado_seccion DROP CONSTRAINT grado_seccion_pkey;
       public            postgres    false    230            �           2606    17032    imparte imparte_pkey 
   CONSTRAINT     {   ALTER TABLE ONLY public.imparte
    ADD CONSTRAINT imparte_pkey PRIMARY KEY (cod_imparte, cod_materia, cod_grado_seccion);
 >   ALTER TABLE ONLY public.imparte DROP CONSTRAINT imparte_pkey;
       public            postgres    false    226    226    226            �           2606    16982    materia materia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.materia
    ADD CONSTRAINT materia_pkey PRIMARY KEY (cod_materia);
 >   ALTER TABLE ONLY public.materia DROP CONSTRAINT materia_pkey;
       public            postgres    false    223            �           2606    17049    nota nota_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.nota
    ADD CONSTRAINT nota_pkey PRIMARY KEY (cod_nota);
 8   ALTER TABLE ONLY public.nota DROP CONSTRAINT nota_pkey;
       public            postgres    false    228            �           2606    16942    profesor profesor_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.profesor
    ADD CONSTRAINT profesor_pkey PRIMARY KEY (cedula_prof);
 @   ALTER TABLE ONLY public.profesor DROP CONSTRAINT profesor_pkey;
       public            postgres    false    216            �           2606    16951     representante representante_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.representante
    ADD CONSTRAINT representante_pkey PRIMARY KEY (cedula);
 J   ALTER TABLE ONLY public.representante DROP CONSTRAINT representante_pkey;
       public            postgres    false    218            �           2606    16958    user user_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (username);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    220            �           2606    16993 !   asigna asigna_ced_estudiante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.asigna
    ADD CONSTRAINT asigna_ced_estudiante_fkey FOREIGN KEY (ced_estudiante) REFERENCES public.estudiante(cedula);
 K   ALTER TABLE ONLY public.asigna DROP CONSTRAINT asigna_ced_estudiante_fkey;
       public          postgres    false    222    224    3233            �           2606    16998    asigna asigna_cedula_prof_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.asigna
    ADD CONSTRAINT asigna_cedula_prof_fkey FOREIGN KEY (cedula_prof) REFERENCES public.profesor(cedula_prof);
 H   ALTER TABLE ONLY public.asigna DROP CONSTRAINT asigna_cedula_prof_fkey;
       public          postgres    false    3227    224    216            �           2606    17072 $   asigna asigna_cod_grado_seccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.asigna
    ADD CONSTRAINT asigna_cod_grado_seccion_fkey FOREIGN KEY (cod_grado_seccion) REFERENCES public.grado_seccion(cod_grado_seccion);
 N   ALTER TABLE ONLY public.asigna DROP CONSTRAINT asigna_cod_grado_seccion_fkey;
       public          postgres    false    3245    224    230            �           2606    17008    asigna asigna_cod_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.asigna
    ADD CONSTRAINT asigna_cod_materia_fkey FOREIGN KEY (cod_materia) REFERENCES public.materia(cod_materia);
 H   ALTER TABLE ONLY public.asigna DROP CONSTRAINT asigna_cod_materia_fkey;
       public          postgres    false    3235    223    224            �           2606    17018 "   cursa cursa_cedula_estudiante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cursa
    ADD CONSTRAINT cursa_cedula_estudiante_fkey FOREIGN KEY (cedula_estudiante) REFERENCES public.estudiante(cedula);
 L   ALTER TABLE ONLY public.cursa DROP CONSTRAINT cursa_cedula_estudiante_fkey;
       public          postgres    false    225    222    3233            �           2606    17023    cursa cursa_cod_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cursa
    ADD CONSTRAINT cursa_cod_materia_fkey FOREIGN KEY (cod_materia) REFERENCES public.materia(cod_materia);
 F   ALTER TABLE ONLY public.cursa DROP CONSTRAINT cursa_cod_materia_fkey;
       public          postgres    false    3235    225    223            �           2606    17077 ,   estudiante estudiante_cod_grado_seccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_cod_grado_seccion_fkey FOREIGN KEY (cod_grado_seccion) REFERENCES public.grado_seccion(cod_grado_seccion);
 V   ALTER TABLE ONLY public.estudiante DROP CONSTRAINT estudiante_cod_grado_seccion_fkey;
       public          postgres    false    230    222    3245            �           2606    16973 +   estudiante estudiante_representante_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_representante_id_fkey FOREIGN KEY (representante_id) REFERENCES public.representante(cedula);
 U   ALTER TABLE ONLY public.estudiante DROP CONSTRAINT estudiante_representante_id_fkey;
       public          postgres    false    222    3229    218            �           2606    17082 &   imparte imparte_cod_grado_seccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.imparte
    ADD CONSTRAINT imparte_cod_grado_seccion_fkey FOREIGN KEY (cod_grado_seccion) REFERENCES public.grado_seccion(cod_grado_seccion);
 P   ALTER TABLE ONLY public.imparte DROP CONSTRAINT imparte_cod_grado_seccion_fkey;
       public          postgres    false    3245    226    230            �           2606    17038     imparte imparte_cod_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.imparte
    ADD CONSTRAINT imparte_cod_materia_fkey FOREIGN KEY (cod_materia) REFERENCES public.materia(cod_materia);
 J   ALTER TABLE ONLY public.imparte DROP CONSTRAINT imparte_cod_materia_fkey;
       public          postgres    false    3235    223    226            �           2606    16983     materia materia_cedula_prof_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.materia
    ADD CONSTRAINT materia_cedula_prof_fkey FOREIGN KEY (cedula_prof) REFERENCES public.profesor(cedula_prof);
 J   ALTER TABLE ONLY public.materia DROP CONSTRAINT materia_cedula_prof_fkey;
       public          postgres    false    3227    223    216            �           2606    17050    nota nota_ced_estudiante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.nota
    ADD CONSTRAINT nota_ced_estudiante_fkey FOREIGN KEY (ced_estudiante) REFERENCES public.estudiante(cedula);
 G   ALTER TABLE ONLY public.nota DROP CONSTRAINT nota_ced_estudiante_fkey;
       public          postgres    false    3233    228    222            �           2606    17055    nota nota_cedula_prof_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.nota
    ADD CONSTRAINT nota_cedula_prof_fkey FOREIGN KEY (cedula_prof) REFERENCES public.profesor(cedula_prof);
 D   ALTER TABLE ONLY public.nota DROP CONSTRAINT nota_cedula_prof_fkey;
       public          postgres    false    216    228    3227            �           2606    17060    nota nota_cod_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.nota
    ADD CONSTRAINT nota_cod_materia_fkey FOREIGN KEY (cod_materia) REFERENCES public.materia(cod_materia);
 D   ALTER TABLE ONLY public.nota DROP CONSTRAINT nota_cod_materia_fkey;
       public          postgres    false    3235    223    228            J      x�KM�0�L�0��0J����� ,`�      T      x������ � �      U      x������ � �      R      x������ � �      Z   X   x�mα�0��W�W����.���8p�%:C���(�K'X�{�~[^ϴ��6�{Y�Sp���j�'��W!0W��+A��+���HIV      V     x�M��n� �����T0��]�q�4���%��� 3���B��Ӿ�ޑ�,tܮg*}m�4����q��i�{�l�H����nf�~�g��
Wc���.�/0�LKW;���W��tt6]�N]Yܪc{��b��E��C�[ǩ����V^��K�[ס�3�MGˢc�ԱªcG��i�ʚMG��uѕ��:�_ul1��+����ֱ�����4�����]���>;��
Go.Z�E��b��E's�y�ʱ����*'����f��h5W�����n��&      S   �   x�E�;R1Dc�:����!lن 
r�F+���J�>�!$؈#�b�z��f�uOW�F�͍hy���h��J����u�+�������3��X-�F���(�����ա�߁��`�m�F}�g�H}��z��IM��kx˛&$��\"�I�þkV�&؈S��)�	��R���3��f-�2��R��K�C?��7
�(�`����LJ���ZI      X      x������ � �      L   ^   x�34261��I��K,J��tIT��KΌ)�25162�tO���I͇ҙ\f����ŉ�ɜ~��%�y\��f���E9�Ŝ���9��I\1z\\\ ���      N      x������ � �      P   �   x�=ʱ
�0 �9����rw�6��������5^�Ŵ�"������Ö Э�b#ձl���tVۦ��6V�A�["�)�`�TsǍ%6��d	�1
80��Ѳ-�<�yѢ�߻g�׻Nsq�#�����/�j*X     