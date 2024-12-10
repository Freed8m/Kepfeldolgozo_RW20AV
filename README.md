# Egyszerűsített képfeldolgozó program<br>
Ez egy képszerkesztő program, egyszerű, gyors, és (egyenlőre) egyszeri operációkhoz.<br><br> Lényege hogy gyors legyen és kicserélje a komplexebb, de lassabb programokat ha csak épp egy egyszerű funkcióra van szükségünk.

# Jellemzők
- Egyszerű felület (Tkinter alapú)
- Megjelenített kép, egyes változások megjelenítése
- Jelenleg egyszeri operációk támogatottak
- Jelenlegi opciók
  - Forgatás (90°, 180°)
  - Kép átméretezés (Bilineáris)
  - Gauss alapú képelmosás
  - Fekete-fehérré váltás
  - Kép-élesítés

# Használat
### Indítás
- Python (3.0 vagy újabb) szükséges
- Terminálban vagy parancssorban futtatandó parancs:
    <br>`python kepfeldolgozo.py`
  <br>vagy
    <br>`py kepfeldolgozo.py`
  <br>vagy
    <br>`python3 kepfeldolgozo.py`
### Általános útmutató  
- A program indításkor rögtön fájlkiválasztáshoz kerülünk
- Miután a kép betölt, két fajta opció-típusról beszélhetünk:
  - A forgatás opciók rögtön exportálják a képet egy szuffixummal, rögtönzött megjelenítés nem lehetséges
  - A többi opció csak akkor exportálódik ha az **'Exportál?'** doboz be van pipálva, ha nincs csak megjeleníti a változásokat
- Az utóbbi opcióknál (kivéve átméretezés) lehetséges a kép megtekintése exportálás nélkül
- Az exportált kép az eredeti képpel megegyező mappába fog kerülni, az operációhoz illően hozzáadott szuffixummal

<br>*Egyenlőre többszöri, 'batch' képfeldolgozás nem lehetséges.*

# Követelmények
- Python 3.0 vagy újabb
  -   Tkinter opcionális modul a python telepítőben
# Előnézet
![Screenshot 2024-12-08 170607](https://github.com/user-attachments/assets/8670eb6f-44ec-4011-822f-d3a22aed8fe3)
