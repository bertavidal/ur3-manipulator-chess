# ur3-manipulator-chess

### Project Description
This project implements an autonomous pickup, inspection, and classification system for a 6-DOF Universal Robots UR3 robotic arm. Operating via TCP/IP socket communication, the manipulator automates the task of picking up a random chess piece from a defined workspace, presenting it for identification, and executing a conditional branch to either sort it into a final line-up or return it to its original location.

The controller coordinates articular joint configuration paths (defined in radians) with external script triggers that command a custom tool gripper to open (`pinza40UR3.py`) and close (`pinza10UR3.py`).

The workflow is organized as an interactive operational loop:
- Localization & Reach: Move from a safe home position to an elevated clearance setup above a randomly chosen piece target.
- Grasping Control: Descend to the piece coordinates, execute a low-level socket binary stream to close the gripper, and retreat safely.
- Inspection Interface: Transport the object to an intermediate checkpoint to reveal the piece configuration, prompting a user validation interface.
- Conditional Sorting: Move along a straight linear trajectory to place the piece in the final line-up if identified as the King; otherwise, revert paths to return the item to the starting grid before opening the gripper.

---

### Descripció del projecte
Aquest projecte implementa un sistema d'inspecció, classificació i manipulació autònoma d'objectes utilitzant un braç robòtic Universal Robots UR3 de 6 graus de llibertat (6-DOF). Funcionant mitjançant comunicació per sockets TCP/IP, el manipulador automatitza la tasca de recollir una peça d'escacs aleatòria, mostrar-la per a la seva identificació i executar una bifurcació condicional per alinear-la en la seva posició final o retornar-la al seu lloc d'origen.

El controlador coordina trajectòries en l'espai de configuracions articulars (definides en radiants) amb l'enviament de scripts externs que ordenen l'obertura (`pinza40UR3.py`) i tancament (`pinza10UR3.py`) d'una pinça de subjecció personalitzada.

El flux de treball està organitzat com un bucle operatiu interactiu:
- Localització i aproximació: Moviment des d'una posició inicial segura (Home) fins a una configuració elevada de seguretat sobre la peça seleccionada.
- Control de subjecció: Descens a les coordenades reals de la peça, enviament d'un flux binari per socket per tancar la pinça i elevació de seguretat.
- Interfície d'inspecció: Transport de la peça a una posició intermèdia de mostra, llançant una interfície de validació interactiva per a l'usuari.
- Classificació condicional: Desplaçament lineal en línia recta per deixar la peça a la fila final si es confirma que és el Rei; en cas contrari, es desfan els passos per retornar-la a la graella inicial abans d'obrir la pinça.

### Estructura del repositori 
- `UR3.py`: Codi de control principal en Python que gestiona la connexió per socket, el càlcul de trajectòries articulars, la tria aleatòria i la lògica de classificació interactiva.
- `pinza10UR3.py`: Script URScript de baix nivell enviat al robot per tancar la pinça a una configuració de subjecció forta de 10 mm.
- `pinza40UR3.py`: Script URScript de baix nivell enviat al robot per obrir la pinça a una configuració d'alliberament de 40 mm.
- `P11 - VC.mlx`: Live Script de MATLAB utilitzat per al modelatge matemàtic previ, proves de cinemàtica de manipulació o funcions auxiliars de visió per computador.
