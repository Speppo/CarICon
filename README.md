# CarICon
Progetto Ingegneria della Conoscenza AA 23/24 di Giuseppe Caggiano matr. 735400 su operazioni di regressione sull'accelerazione di un auto

# Configurazioni iniziali
Installare SWI-Prolog dal sito ufficiale https://www.swi-prolog.org/download/stable, per utilizzare la libreria pyswip.
Successivamente, dopo aver aperto il progetto con l’IDE preferito, avviare lo script install.py per installare le varie librerie.

# Struttura del progetto
-install.py: installa tutte le librerie necessarie per l'esecuzione del progetto.
-datasets: contiene il dataset originale e gli altri generati. 
-grafici: contiene i file utilizzati per generare i grafici.
-risultati: contiene i csv di tutti i risultati trovati per ogni combinazione di parametri.
-documentazione: contiene documentazione del progetto.
-adaboost.py, decision_tree_learner.py, knn.py, random_forest.py: implementano i modelli di apprendimento supervisionato.
-k_means.py: implementa modello di apprendimento.
-kb.py: genera il Prolog
-preprocessing.py: esegue operazioni di preprocessing sul dataset iniziale
