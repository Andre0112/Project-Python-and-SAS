#1
libname proiect '/home/u64185848';

FILENAME COMENZI '/home/u64185848/comenzi_pr.csv';

PROC IMPORT DATAFILE=COMENZI
OUT=proiect.Comenzi
DBMS=CSV
REPLACE;
GETNAMES=YES;
DELIMITER=',';
RUN;


proc print data=proiect.Comenzi(obs=15);
    title "Primele 15 observații din datasetul Comenzi";
run;

DATA proiect.info_angajati_proiect;
INFILE '/home/u64185848/info_angajati_proiect.txt';
INPUT Nume $ Prenume $ Departament $ Salariu $ Varsta $ Vechime_loc_munca;
RUN;

proc print data=proiect.info_angajati_proiect(obs=15);
    title "Primele 15 observații din datasetul info_angajati_proiect";
run;


#2
FILENAME COMENZI '/home/u64185848/comenzi_pr.csv';

PROC IMPORT DATAFILE=COMENZI
	OUT=proiect.COMENZI
	DBMS=CSV
	REPLACE;
	GETNAMES=YES;
	DELIMITER=',';
RUN;

DATA proiect.comenzi;
	LENGTH Nume_client $150 Denumire_produs $150 Categorie $35;
	INFILE '/home/u64185848/comenzi_pr.csv' DLM=',' FIRSTOBS=2 DSD;
	INPUT Nume_client $ Cod_client  Denumire_produs $ Brand $ Categorie $ 
	      Cantitate_comandată Preț_unitar Procent_de_reducere Pret_final Total_comandă;
RUN;

PROC FORMAT;
	VALUE CantitateFmt 
		low - <10 = 'Mica'
		10 - 100 = 'Medie'
		100 <- high = 'Mare';
RUN;

PROC PRINT DATA=proiect.comenzi;
	VAR Nume_client Denumire_produs Categorie Cantitate_comandată;
	FORMAT Cantitate_comandată CantitateFmt.;
	TITLE "Detalii comenzi clienți";
RUN;

#3
DATA proiect.info_angajati;
	LENGTH Nume $15 Prenume $15 Departament $15;
    INFILE '/home/u64185848/info_angajati_proiect.txt';
    INPUT Nume $ Prenume $ Departament $ Salariu Varsta Vechime_loc_munca;

    DO;
        IF Vechime_loc_munca = 1 THEN 
        Bonus = Salariu * 0.10;
        ELSE IF 1 < Vechime_loc_munca <= 3 THEN Bonus = Salariu * 0.15;
        ELSE IF 3 < Vechime_loc_munca <= 5 THEN Bonus = Salariu * 0.25;
        ELSE IF Vechime_loc_munca > 5 THEN Bonus = Salariu * 0.35;
        ELSE Bonus = .;
    END;
RUN;

PROC PRINT DATA=proiect.info_angajati;
    VAR Nume Prenume Departament Salariu Vechime_loc_munca Bonus;
    TITLE "Bonusul angajatilor in functie de vechimea de la locul de munca";
RUN;


#4
PROC PRINT DATA=proiect.info_angajati;
	WHERE Departament= 'HR' AND Salariu < 4000;
	VAR Nume Prenume Departament Salariu;
	TITLE "Angajati departament HR";
RUN;

#5
Data proiect.comenzi;
	LENGTH Nume_client$150.;
	LENGTH Denumire_produs$150.;
	LENGTH Categorie$35.;
	INFILE '/home/u64185848/comenzi_pr.csv' dlm=',' firstobs=2;
	INPUT Nume_client $ Cod_client Denumire_produs $ Brand $ Categorie $ Cantitate_comandată
	Preț_unitar Procent_de_reducere Preț_final Total_comandă;
	TITLE "Detalii comenzi clienți";
RUN;

PROC PRINT DATA=proiect.comenzi;
	VAR Denumire_produs Brand Categorie Cantitate_comandată Total_comandă;
	SUM Total_comandă;
	WHERE Categorie="Instrumente de scris";
	TITLE "Suma totala incasata de comenzile din categoria Instrumente de scris";
RUN;


#6
PROC SQL;
	CREATE TABLE comenzi_clienti AS
	SELECT * 
	FROM proiect.comenzi;
QUIT;

PROC SQL;
	CREATE TABLE raport_sumarizat_clienti AS 
	SELECT nume_client, cod_client, 
	       SUM(total_comandă) AS total_comenzi, 
	       COUNT(*) AS numar_comenzi
	FROM comenzi_clienti
	GROUP BY nume_client, cod_client;
QUIT;

PROC PRINT DATA=raport_sumarizat_clienti;
	TITLE "Raportul comenzilor pentru fiecare client";
	VAR cod_client nume_client total_comenzi numar_comenzi;
RUN;


DATA angajati_numeric;
	SET proiect.info_angajati_proiect;
	salariu_numeric = input(Salariu, best12.);
RUN;


PROC SQL;
	CREATE TABLE raport_sumarizat_angajati AS 
	SELECT departament, 
	       SUM(salariu_numeric) AS salariu_total, 
	       COUNT(*) AS numar_angajati
	FROM angajati_numeric
	GROUP BY departament;
QUIT;

PROC PRINT DATA=raport_sumarizat_angajati;
	TITLE "Raport sumarizat al salariilor si numarului de angajati pe departament";
	VAR departament salariu_total numar_angajati;
RUN;

#7
DATA proiect.info_angajati_proiect2;
	INFILE '/home/u64185848/info_angajati_proiect2.txt';
	INPUT Nume $ Prenume $ Departament $ Salariu Varsta Vechime_loc_munca Feedback;

	IF Feedback = 0 THEN Feedback = .;
RUN;

PROC PRINT DATA=proiect.info_angajati_proiect2;
	TITLE "Feedback angajati despre ceea ce le ofera compania";
RUN;

#8
PROC FREQ DATA=proiect.comenzi;
	TABLES Brand * Cantitate_comandată/ ncol nrow nopercent;
	FORMAT Total_Comandă nivel.;
	TITLE "Raport privind totalul de comenzi";
RUN;


#9
PROC UNIVARIATE DATA=proiect.info_angajati PLOT;
	VAR Salariu;
	TITLE "Statistici descriptive referitoare la salariile angajatilor Office Direct";
RUN;

#10
PROC SGPLOT DATA=proiect.comenzi;
	VBAR Brand / Group= Total_comandă;
	TITLE 'Raport Branduri privind totalul comenzilor';
RUN;
QUIT;
