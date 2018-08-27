<img src=Pictures\Logo.jpg align="right"/>

# Zbuduj własny pupilometr!
Projekt "**Pupilometr SE** *(Single-Eye)*" zakłada stworzenie własnego pupilometru (*urządzenia do pomiaru rozwarcia źrenicy*) w oparciu o platformę *Raspberry Pi* oraz oprogramowanie go z użyciem języka Python. Główną funkcją wykonanego urządzenia mają być pomiary stanów emocjonalnych związanych ze zróżnicowanymi stymulacjami.

W poniższych sekcjach omówione zostaną m.in. kwestie techniczne, wykonanie i oprogramowanie okularów pomiarowych oraz funkcje programu. Jeśli preferujesz bardziej wizualne przedstawienie tematyki tego projektu, zachęcam do obejrzenia skróconej prezentacji wideo, w której omówione zostało konkretne wykorzystanie powyższego projektu w tematyce rozpoznawania emocji.<br/><br/>

<div style=text-align:center;"> <a href="https://youtu.be/x26nm6H7VLs"> <img src=Pictures\Icon.jpg style="height: 400px"/> </a> </div> 

# Spis treści
- [Podstawy naukowe](#podstawy-naukowe)
  * [Źrenica](#Źrenica)
  * [Pupilometria](#pupilometria)
  * [Budowa pupilometru](#budowa-pupilometru)
- [Wykonanie](#wykonanie)
  * [Elementy układu](#elementy-uk%C5%82adu)
  * [Konstrukcja okularów pomiarowych](#konstrukcja-okularów-pomiarowych)
- [Przeprowadzanie procedury pomiaru ze stymulacją](#przeprowadzanie-procedury-pomiaru-ze-stymulacją)
- [Oprogramowanie układu rejestrującego](#oprogramowanie-układu-rejestrującego)
  * [Część ustawień wstępnych](#część-ustawień-wstępnych)
  * [Część rejestracji ze stymulacją](#część-rejestracji-ze-stymulacją)
  * [Część obróbki i pomiarów](#część-obróbki-i-pomiarów)
  * [Część prezentacji i zapisu](#część-prezentacji-i-zapisu)
- [Przykładowe badania](#przykładowe-badania)


# Podstawy naukowe
W tej części opisane zostały podstawy naukowe działania pupilometrii. Jeśli jesteś zaznajomiony z tematem - możesz śmiało odpuścić tę część, chociaż brak znajomości zaprezentowanych poniżej zagadnień może uniemożliwić Ci zrozumienie niektórych z konceptów zaprezentowanych w późniejszych punktach tej dokumentacji.


## Źrenica
Przedmiotem badań pupilometrycznych jest źrenica, zatem warto pokrótce opisać jej budowę, rolę oraz mechanizm działania. 
Źrenicą nazywamy otwór w tęczówce znajdujący się w centralnej części oka, przez który światło dostaje się do jego wnętrza. Jej rozmiar waha się od 2 mm do 8 mm, w zależności od czynników zewnętrznych (m.in. ilości światła czy stanu akomodacji oka). Jest on kontrolowany poprzez działające antagonistycznie mięśnie tęczówki, zwieracz i rozwieracz. 


<p align="center">
  <img width="600" height="200" src=Pictures\ZrenicaIdea.jpg>
</p>

Zwężanie źrenicy realizowane jest przez mięsień zwieracz źrenicy (łac. *musculus sphincter pupillae*), zbudowany z włókien mięśniowych gładkich w postaci płaskiego pierścienia umiejscowionego w tylnej części zrębu tęczówki. Unerwiony jest on przez przywspółczulny układ nerwowy, odpowiedzialny w dużej mierze za utrzymanie homeostazy organizmu. Droga mózgowa zwężania źrenicy rozpoczyna się od impulsu nerwowego spowodowanego pojawieniem się światła na siatkówce. Impuls ten - poprzez nerw wzrokowy - przechodzi do skrzyżowania nerwów wzrokowych, gdzie następuje kombinacja sygnałów z obojga oczu i jego reorganizacja. Informacja ta jest dalej wysyłana do jądra przedpokrywkowego, odpowiednio z lewej części pola widzenia do jądra położonego w prawej półkuli, a z prawej części widzenia – do jądra położonego w lewej półkuli. Następnie, połączone z lewej i prawej części pola widzenia sygnały są wysyłane do jąder Edingera-Westphala, skąd – poprzez nerw okołoruchowy – dostają się one do zwojów rzęskowych położonych tuż za lewym i prawym okiem. Stąd informacja, za pomocą nerwów rzęskowych krótkich, trafia do mięśnia zwieracza źrenicy.

Rozszerzanie źrenicy kontrolowane jest poprzez mięsień rozwieracz źrenicy (łac. *musculus dilatator pupilae*), również zbudowany z włókien mięśniowych gładkich, lecz rozciągających się promieniście, od środka źrenicy ku obwodowi tęczówki. Mięsień ten jest unerwiony przez współczulny układ nerwowy, odpowiadający za mobilizację organizmu. Droga mózgowa rozszerzania źrenicy rozpoczyna się w podwzgórzu oraz miejscu sinawym. 
Obie te struktury – z punktu widzenia opisywanego odruchu – pełnią podobną rolę, reagując na pobudzenia organizmu (rozbudzenie, czujność) i przekazując sygnał do słupa pośrednio-bocznego. Stąd jest on przekazywany dalej, do zwoju szyjnego górnego i – poprzez skomplikowaną strukturę nerwową – trafia do mięśnia rozwieracza źrenicy.
Jak można dostrzec, unerwienie przeciwstawnych (w rozumieniu roli) mięśni sterujących stopniem rozwarcia źrenicy poprzez antagonistycznie względem siebie działające układy współczulny i przywspółczulny wskazywać może na to, iż reakcja źrenicy będzie powiązana z reakcjami ciała na bodźce zewnętrzne.

## Pupilometria

**Badanie polegające na pomiarze zmienności wielkości średnicy pola źrenicy w czasie nazywamy pupilometrią**. Rozmiar źrenicy zależy od trzech czynników: od oświetlenia siatkówki, stanu akomodacyjnego oraz sytuacji emocjonalno-sensorycznej.

Pierwszy czynnik nazywany jest **reakcją źreniczną na światło** (PLR, z ang. *Pupil Light Reflex*). Polega on na zwężeniu źrenicy w odpowiedzi na światło. Detektorem w tym odruchu (reakcji) jest siatkówka, w skład której wchodzą 3 typy fotoreceptorów: czopki, pręciki oraz światłoczułe komórki zwojowe. Względna absorpcja tych fotoreceptorów została zaprezentowana poniżej.

<p align="center">
  <img width="800" height="400" src=Pictures\WzglednaAbsorpcja.jpg>
</p>

Czopki są receptorami odpowiedzialnymi za widzenie barwne przy dobrych warunkach oświetleniowych. U ludzi, występują trzy typy czopków, które różnią się czułością na promieniowanie: <u>OPN1LW</u> (λ = około 590 nm, oznaczona literą D), <u>OPN1MW</u> 
(λ = około 540 nm, oznaczona literą Ś) oraz <u>OPN1SW</u> (λ = około 450 nm, oznaczona literą K). Ich liczbę szacuje się na około 4,5 miliona (większość zgromadzona jest w obrębie plamki żółtej). Za widzenie skotopowe (w skrajnie niekorzystnych warunkach oświetleniowych) odpowiadają pręciki (oznaczone skrótem Pr), ze względu na swoją zdecydowanie lepszą czułość na światło w porównaniu do czopków. Ulokowane są one głównie na obrzeżach siatkówki. ipRGCs to melanopsynowe komórki zwojowe siatkówki, które – prócz odbierania bodźców z czopków i pręcików – zawierają również własny fotopigment, zwany melanopsyną. Grupa ta uzupełnia system widzenia wzrokowego poprzez rejestrację zmian intensywności promieniowania w czasie, co wynika z ich zdecydowanie wolniejszego czasu reakcji w porównaniu do pozostałych fotoreceptorów. Czopki i pręciki odpowiadają za wstępne zwężenie się źrenicy (0,2 s - 1,5 s), jednak bardzo szybko ulegają wysyceniu. Za podtrzymywanie tego zwężenia przy stale obecnym świetle odpowiadają natomiast ipEGCs. Sam PLR jest odruchem bardzo silnym; przykładowo wpływ kognitywnych czynników na wielkość zmiany źrenicy przy tym odruchu szacuje się na od 1 procenta do 5 procent. Na poniższym rysunku zaprezentowano uśrednioną odpowiedź 10 reakcji PLR na 10 sekundowy błysk światła czerwonego oraz niebieskiego. Oś X przedstawia czas, który upłynął od momentu stymulacji trwającej 10 sekund. Oś Y przedstawia względną zmianę, proporcjonalną do średnicy źrenicy przed pomiarem. Na wykresie zaznaczono również błąd standardowy pomiarów.

<p align="center">
  <img width="800" height="400" src=Pictures\PLR_wykres.jpg>
</p>

Drugim czynnikiem wpływającym na rozszerzenie źrenicy, jest jej **odpowiedź na stan akomodacji oka** (PNR, z ang. *Pupil Near Response*). Objawia się on zmniejszeniem średnicy podczas patrzenia na obiekty położone blisko oka oraz jej zwiększeniem podczas patrzenia w dal. Jest on częścią tzw. triady odpowiedzi bliży wzrokowej, zaraz obok nastawności oka oraz konwergencji, które zazwyczaj występują razem. Jego główną rolą jest zwiększanie głębi ostrości przy widzeniu z bliskiej odległości. Jest to jeden z najsłabiej poznanych do tej pory czynników. Na poniższym rysunku zaprezentowano przykładową odpowiedź PNR dla 10 pomiarów. Oś X przedstawia czas od momentu stymulacji o schemacie 10 sekundowego przejścia skupienia wzroku z 2 metrów do 0,1 metra oraz późniejszym powrocie skupienia wzroku do 2 metrów. Oś Y przedstawia względną zmianę proporcjonalną do średnicy źrenicy przed pomiarem. Na wykresie zaznaczono błąd standardowy pomiarów. 

<p align="center">
  <img width="800" height="400" src=Pictures\AkomodacjaWykres.jpg>
</p>

Ostatnim czynnikiem, będącym podstawą rozważań w tej pracy, jest **odpowiedź źrenicy na szeroko pojętą sytuację emocjonalno-sensoryczną** (PPR, z ang. *Psychosensory Pupil Reaction*). Ujawnia się ona w wielu reakcjach związanych ze stymulacją, myśleniem czy emocjami, zgodnie z myślą sformułowaną w 1958 roku przez Irene Loewenfeld: *„Wszystko, co w jakiś sposób aktywuje umysł bądź zwiększa jego ładunek pracy, znajduje odzwierciedlenie w rozszerzeniu źrenicy”*. Z wszystkich trzech czynników, PPR ma najbardziej subtelny wpływ na rozszerzenie źrenicy, stąd – mimo wielu badań – ciężko jest powiązać go z konkretnymi reakcjami emocjonalnymi. Samo zagadnienie roli zmian rozmiaru źrenicy w odpowiedzi na stany psychosensoryczne, również nie zostało do końca poznane – postuluje się nawet, iż zmiany te, z punktu widzenia funkcjonalnego, nie grają żadnej roli i są jedynie efektem ubocznym aktywności mózgowej. Mimo to, niektórzy naukowcy twierdzą, iż rzeczywista rola stanu zwężenia źrenicy może być trudna do zmierzenia, m.in. ze względów etycznych w wywoływaniu skrajnych emocji, np. lęku. Na poniższym rysunku zaprezentowano przykładową odpowiedź PPR, złożoną z 25 pomiarów, dla jednosekundowego impulsu białego szumu. Oś X przedstawia czas od momentu rozpoczęcia stymulacji. Oś Y przedstawia względną zmianę proporcjonalną do średnicy źrenicy przed pomiarem. Na wykresie zaznaczono błąd standardowy pomiarów.

<p align="center">
  <img width="800" height="400" src=Pictures\DzwiekowyWykres.jpg>
</p>

Należy również wspomnieć o zjawisku **samoistnych fluktuacji źrenicy**, które pojawiają się bez wpływu zewnętrznych czynników. Postuluje się, iż są one wynikiem głównie zmęczenia bądź senności. Generalnie rzecz ujmując – samoistne fluktuacje odzwierciedlają poziom pobudzenia badanego.

## Budowa pupilometru
Z punktu widzenia budowy pupilometru, najważniejszym jego elementem jest **rejestrator obszaru źrenicy** – jego rolę pełni zazwyczaj kamera o wysokiej rozdzielczości i szybkości rejestracji obrazu. Ze względu na opisany powyżej odruch PLR, układ taki powinien mieć możliwość rejestracji obrazu przy braku dostępności światła widzialnego (ze względu na brak reakcji PLR dla światła spoza pasma rejestracji receptorów). W takim wypadku, potrzebne może okazać się również dodatkowe źródło światła IR. Prócz układu rejestrująco-oświetlającego, w zależności od wymagań stawianym badaniom, może okazać się także konieczne wyeliminowanie efektu PNR, najczęściej poprzez zastosowanie punktu fiksacji dla oka. Pomiar może odbywać się zarówno na obydwu źrenicach, jak i – dzięki istnieniu zjawiska <u>*konsensualności*</u>, czyli reakcji obuocznej na bodziec dostarczony do jednego oka – na wybranej źrenicy. Dodatkowo, w nowoczesnych jednostkach pupilometrycznych znaleźć można także układ odpowiedzialny za obróbkę i zapis zarejestrowanego obrazu, a nawet za automatykę dokonywania pomiarów.
Sama procedura pomiaru, jak i warunki pomiarowe, nie są ściśle określone i w zależności od celu wykonywania badań, mogą się od siebie różnić. Dla przykładu, kliniczna metoda badania zakłada kolejno zlokalizowanie źrenicy, ocenę jej kształtu i pozycji, a następnie sprawdzenie reakcji na bodziec świetlny. Pomiar taki powinien odbywać się w ciemnym pomieszczeniu, przy skupieniu wzroku pacjenta na odległym obiekcie oraz braku jakiejkolwiek dodatkowej stymulacji (np. dotyku). Sama procedura polega na wielokrotnym oświetlaniu źrenicy i zapisywaniu oceny reakcji w skali 1-4, a następnie ponownej ocenie zachowania źrenicy, tym razem przy skupieniu pacjenta na obiekcie położonym od 15cm do 20cm od oka. Dla odmiany, w badaniach naukowych stosuje się pomiar średnicy źrenicy za pomocą metody manualnej bądź automatycznej (wspomaganej komputerowo), dodatkowo pomiar odbywa się w domenie czasowej. Szczególnie ważne okazuje się jednak przygotowanie stymulacji do badań – w metodykach wielu prac można zauważyć m.in. wyrównywanie jasności prezentowanych zdjęć stymulujących bądź normalizowanie głośności ścieżek audio dla badań nad reakcją powiązaną ze stymulacją dźwiękową.

# Wykonanie
W tej części opisane zostały praktyczne wskazówki wykonania układu pomiarowego wraz z doborem części i schematem połączeń.
## Elementy układu
* **Raspberry Pi 3B**

Istnieje możliwość wykorzystania innego układu z rodziny Raspberry Pi, jednak może powodować to problemy z kopatybilnością bądź szybkością działania - więcej na ten temat w punkcie "[Przykładowe badania](#przykładowe-badania)".

* **Raspberry Pi NoIR Camera HD v2 8MPx**

Wybór tej kamery podyktowany był wysoką rozdzielczość układu, dużą szybkość rejestracji obrazu oraz możliwość działania w warunkach braku światła widzialnego. Dodatkowo, ze względu na mocno ograniczone zasoby Raspberry Pi, ważne było także sprzętowe wsparcie kamery przez tenże układ, zwłaszcza przy trybach rejestracji w wysokich rozdzielczościach.

* **Google CardBoard**

W tym projekcie wykorzystana została pierwsza wersja tych okularów. W punkcie "[Konstrukcja okularów pomiarowych](#konstrukcja-okularów-pomiarowych)" omówione zostały modyfikacje przeprowadzone w celu lepszego dostosowania okularów do pomiarów pupilometrycznych.

* **Dioda IR oraz LED**

Wybór konkretnych parametrów pracy diody IR (doświetlającej) oraz LED (stymulującej) podyktowany jest budową oraz rozmieszczeniem diod w okularach. W toku prac nad układem testowane były różne rozwiązania i żadne z nich nie sprawiło problemów z działaniem całego pupilometru.

* **Sluchawki**

Słuchawki stosowane są w celu stymulacji audio. Jedynym wymaganiem jest złącze miniJack, kompatybilne z Raspberry Pi.

* **Inne peryferia**

W celu podglądu obrazu przed rozpoczeciem badania, potrzebny jest dowolny monitor z wyjściem HDMI. Należy również pamiętac o urządzeniach wejściowych, takich jak klawiatura i myszka oraz zasilaniu. <br/><br/>

--- 
<br/>Poprawnie podłączony układ powinien wyglądać następująco: <br/><br/>


<p align="center">
  <img width="700" height="700" src=Pictures\Podlaczanie.jpg>
</p><br/><br/>

Schemat podłączeń diod:<br/><br/>

<p align="center">
<img width="300" height="300" src=Pictures\Diody.jpg>
</p><br/><br/>

Ideowy schemat podłączenia Raspberry: <br/><br/>

<p align="center">
<img width="500" height="500" src=Pictures\IdeowyPodlaczen.jpg>
</p>

## Konstrukcja okularów pomiarowych

W toku prac nad układem, koniecznym okazało się wyeliminowanie wpływu odruchu PLR, będącego wielokrotnie mocniejszą reakcją źrenicy w porównaniu do efektów emocjonalnych. Pierwszym przystosowaniem było znalezienie kamery, zdolnej do rejestracji obrazu w podczerwieni, co zostało opisane w poprzednim punkcie. Dla drugiego przystosowania - zapewnienia warunków braku dostępności światła widzialnego - pojawiły się dwie propozycje; pierwsza z nich polega na modyfikacji sposobu przeprowadzania eksperymentów poprzez wprowadzenie wymogu rejestracji w pomieszczeniach całkowicie zaciemnionych. Rozwiązanie takie niestety wprowadzałoby konieczność dostosowywania pomieszczeń do badania poprzez wyeliminowanie wszystkich źródeł światła widzialnego, co w dłuższej perspektywie byłoby uciążliwe, a w niektórych przypadkach wręcz niemożliwe. 
Dodatkowo, konieczne byłoby każdorazowe dostosowywanie kamery pod ułożenie pacjenta, a sama jego pozycja byłaby wymuszona przez umiejscowienie układu, co wprowadzałoby dodatkowe czynniki mogące zakłócić pomiar pupilometryczny. Z tego powodu, tworząc układ pomiarowy, postanowiono zaprojektować rozwiązanie zamknięte, pozwalające na odseparowanie oczu od bodźców świetlnych. Do tego celu wykorzystano szablon projektu *Google Cardboard*, służącego pierwotnie jako kartonowa obudowa dla telefonów wykorzystujących wirtualną rzeczywistość, który został zmodyfikowany na potrzeby projektowanego układu. 

Do modyfikacji przeprowadzonych na okularach *Google Cardboard* należą:
* usunięcie dwóch wbudowanych soczewek,
* powiększenie pozostałego po soczewce lewego otworu celem lepszego doświetlenia rejestrowanego oka,
* wycięcie kwadratowego otworu w przedniej lewej części Cardboard, umożliwiającego podłączanie układu bez konieczności otwierania całej konstrukcji,
* stworzenie dedykowanego panelu (z tablicy korkowej) dla kamery i diody z wyprowadzeniem potrzebnych konektorów, nakładanego na w/w otwór, posiadającego możliwość prostej modyfikacji lub wymiany,
* umieszczenie dedykowanego panelu w strefie wewnętrznej, umożliwiając tym samym wertykalną zmianę ustawienia kamery w zależności od położenia oka,
* stworzenie panelu (z tablicy korkowej) z diodą służącą do stymulacji świetlnej wraz z wyprowadzeniem potrzebnych konektorów,
* wycięcie mniejszego otworu w przedniej prawej części celem umożliwienia akomodacji oka na obiekcie położonym z dala od badanego,
* dodanie opaski z rzepem odpowiadającej za utrzymywanie w odpowiedniej pozycji całego zestawu z możliwością jej dopasowania do wielkości głowy badanego,
* zwiększenie przyczepności powierzchni pierwotnie klejonych poprzez zastosowanie taśmy dwustronnej,
* zaklejenie otworów montażowych, przez które dostawało się światło do wewnętrznej części,
* dodanie gąbek w części styku konstrukcji z głową oraz nosem badanego celem zwiększenia wygody i dodatkowej eliminacji niepożądanych źródeł światła,
* zmiana kolorystyki Cardboard na ciemną.

Powyższe zmiany pozwoliły na niemal całkowite wyeliminowanie światła dostającego się do środkowej części Cardboard. Dodatkowo, stała pozycja kamery umożliwiła redukcję obszaru rejestracji, co pozwoliło z kolei na zwiększenie prędkości rejestracji oraz jakości obrazu. Poniżej zaprezentowano rzeczywisty wygląd zbudowanego rozwiązania.<br/><br/>

<p align="center">
  <img width="700" height="500" src=Pictures\OkularyPrzod.JPG>
</p>

<p align="center">
  <img width="700" height="500" src=Pictures\OkularyTyl.JPG>
</p>

# Przeprowadzanie procedury pomiaru ze stymulacją

Poniżej opisany został sposób przygotowania do badania pupilometrycznego ze stymulacją w oparciu o projekt Pu**pi**lometr <u>Single Eye</u>.

Mimo, iż urządzenie posiada zabezpieczenia przed dostawaniem się niepożądanego światła do jego wnętrza, pomiary należy przeprowadzać najlepiej w zaciemnionym pomieszczeniu, wolnym od obecności niepożądanych dźwięków i innych stymulacji mogących wpłynąć na badania. Badany powinien usiąść w wygodnym miejscu, założyć na głowę urządzenie (dopasowując siłę zapięcia paska do własnych preferencji) oraz – w przypadku stymulacji audio – także słuchawki. Naprzeciwko badanego, w niewielkiej odległości, powinien znajdować się lekko podświetlony i stateczny obiekt, na którym badany będzie mógł skupić swój wzrok. Należy upewnić się, iż badanemu nie przeszkadzają żadne niepożądane bodźce zewnętrzne, np. zwisające bezwładnie kable bądź ucisk pochodzący z nieprawidłowego umieszczenia okularów badawczych.
Dodatkowo, wskazane jest usunięcie makijażu oczu, które może wpływać na wynik badania.

Następnym krokiem jest poinstruowanie badanego o podmiocie badań i stosowanych stymulacjach. Należy wykluczyć wszelkie przeciwwskazania do przeprowadzenia badania, szczególnie przy używaniu stymulacji typu *startle*, takich jak choroby serca, astma, nadciśnienie, epilepsja czy fobie. Badanego należy poinstruować, by na czas badania zaprzestał mrugania, a wzrok – przez otwór w prawej części okularów – skupił na postawionym tam uprzednio obiekcie.
Przed rozpoczęciem badania należy upewnić się, iż układ został podłączony poprawnie. Szczególną uwagę należy skierować na połączenia przewodów diod oraz kamery – jakiekolwiek błędy w tej materii skutkować będą nieprawidłowym działaniem.

Aby uruchomić program główny badania, należy skorzystać z narzędzia *Konsola* dostępnego w menu głównym systemu Raspbian (zakładka Akcesoria). Przed uruchomieniem skryptu należy przejść do katalogu, w którym się on znajduje korzystając z polecenia cd, przykładowo:

```txt
cd home/pi/Desktop/Pupilometr
```

#### Program posiada 5 opcji badania:

* **nostimulation** – badanie pozbawione bodźca z możliwością ustalenia czasu pomiaru, przydatne m.in. w badaniach opisanych wcześniej samoistnych fluktuacji źrenicy bądź jako sprawdzenie poprawności działania urządzenia.
* **randomsound** – badanie z losowo wybraną stymulacją dźwiękową z bazy *IADS2*, poprzedzoną czterosekundowym białym szumem (2s narastania oraz 2s utrzymywania poziomu głośności) dające możliwość ustawienia czasu rejestracji przed oraz po stymulacji.
* **startle** – badanie mające na celu wywołanie gwałtownej reakcji zaskoczenia poprzez odtworzenie niezapowiedzianego przeraźliwego dźwięku (o długości 1s). Element losowości kontrolowany jest poprzez podanie zakresu czasowego, w przedziale którego wylosowany będzie moment odtworzenia dźwięku.
* **mysound** – badanie z wybraną przez użytkownika stymulacją dźwiękową z bazy IADS2, poprzedzoną czterosekundowym białym szumem (2s narastania oraz 2s utrzymywania poziomu głośności) dającą możliwość ustawienia czasu rejestracji przed oraz po stymulacji. Istnieje opcja dodania swojego własnego dźwięku stymulacji poprzez skopiowanie go do folderu bazy IADS2.
* **light** – badanie odruchu PLR za pomocą wbudowanej w prawej części okularów białej diody z możliwością wyboru czasu rejestracji przed i po stymulacji oraz rozpiętości czasowej, w której dioda pozostaje uaktywniona.

**IADS2** (z ang. *International Affective Digitized Sounds*) jest bazą stymulacji emocjonalnych, opublikowaną przez NIMH Center for Emotion and Attention (University of Florida) celem polepszenia jakości przeprowadzanych badań nad emocjami i ustandaryzowania wyników pomiędzy różnymi badaniami. Zawiera ona ponad 150 znormalizowanych dźwięków o zbadanych wśród obu płci poziomach „pleasure” (przyjemności), „arousal” (pobudzenia) oraz „dominance” (dominacji). <u>Ze względu na ograniczenia licencyjne, nie jest ona dołączona do tego repozytorium!</u></br></br>

<p align="center">
  <img width="700" height="200" src=Pictures\ArgumentyProgramuProste.JPG>
</p> </br></br>

Uruchomienie programu odbywa się poprzez wpisanie kolejno argumentów w konsoli, zaprezentowanych powyżej. Dla przykładu, uruchomienie badania bez stymulacji trwającego 3 sekundy wygląda następująco:
```txt
sudo python3 Pupilometr.py badany nostimulation 3
```
Poprawne rozpoczęcie programu sygnalizowane jest poprzez napis **„Uruchomiono pupilometrię!”**. W dalszej części następuje włączenie kamery celem dostosowania się jej do warunków panujących wewnątrz urządzenia (trwające standardowo 5 sekund), podczas których badający ma możliwość podejrzenia na ekranie podłączonego monitora obrazu z kamery i wprowadzenia ewentualnych poprawek (bądź przerwania badania w przypadku napotkania większych problemów). Na tym etapie warto zwrócić uwagę na umieszczenie źrenicy w obszarze badania – **powinna być ona położona jak najbliżej środka obrazu**. Korekcje w położeniu poziomym można wprowadzać poprzez lekkie przesunięcie płyty korkowej, dostępnej po otwarciu przedniej części okularów, zamocowanej na rzep. Ważne jest też sprawdzenie poprawności doświetlenia – powinno ono obejmować cały obszar rejestracji, nie pozostawiając obszarów o czerni obrazu porównywalnej do źrenicy. W takiej sytuacji należy zmienić kierunek świecenia diody doświetlającej tak, by cały obszar był dobrze doświetlony. Poniżej zaprezentowano kolejno obrazy: prawidłowy, o złym doświetleniu oka oraz o źle umieszczonej źrenicy.</br></br>

<p align="center">
  <img width="600" height="200
  " src=Pictures\ObrazyOka.jpg>
</p>

**Dalsza część programu jest w pełni automatyczna** – w zależności od wybranego badania, ukazywać się będą komunikaty mówiące o aktualnym etapie działania układu. 
Po zakończonej rejestracji oka, samodzielnie rozpocznie się procedura pomiarów obszaru źrenicy, z charakterystycznym przewijaniem się linii opisujących każdy pomiar (wraz z kolorowym zaznaczeniem podejrzenia jego poprawności). Po zakończeniu sekcji pomiarowej, w konsoli wyświetlone zostanie podsumowanie całych pomiarów. Przykładowy efekt działania skryptu (dla ustawień nostimulation 3) zaprezentowano na poniżej.</br></br>

<p align="center">
  <img width="600" height="800
  " src=Pictures\ProgramWykonany.jpg>
</p></br>

Wraz z zakończeniem pomiarów, powinno pojawić się także okno z wykresem zmienności średnicy źrenicy w czasie. Okno to jest interaktywne – możliwe jest m.in. przybliżanie i oddalanie konkretnych obszarów wykresu, podgląd położenia pojedynczych punktów pomiarowych na osiach czy zmiany położenia samego wykresu w oknie. 
W zależności od wybranej opcji pomiarowej, na wykresie kolorowymi liniami zaznaczane są początek rozpoczęcia stymulacji oraz jej koniec, a w przypadku stymulacji z poprzedzającym je białym szumem kolejno początek rozpoczęcia szumu, początek stymulacji oraz koniec.</br></br>

<p align="center">
  <img width="400" height="400 " src=Pictures\PrzykladowyWykres.jpg>
</p></br>

Dodatkowo, w osobnym folderze, opatrzonym m.in. datą badania, tworzony jest katalog zawierający wszystkie zdjęcia pomiarowe, wygenerowany wykres w formie ilustracji oraz plik w formacie Excel zawierający opis wykonanego badania oraz wszystkie pomiary, który służyć może do późniejszej analizy otrzymanych wyników.</br></br>

<p align="center">
  <img width="400" height="400 " src=Pictures\PlikWynikowy.jpg>
</p></br>

# Oprogramowanie układu rejestrującego
Działanie programu układu można podzielić na cztery części: ustawień wstępnych, rejestracji ze stymulacją, pomiarów źrenicy oraz prezentacji/zapisu wyników działania układu. Części te, wraz z graficznym wyróżnieniem etapów przetwarzania obrazu, przedstawiono poniżej.

<p align="center">
  <img width="700" height="500" src=Pictures\SchematProgramu.JPG>
</p>

> **Uwaga edytorska:** W celu zachowania przejrzystości poniższego tekstu <u>bez wklejania części kodu programu</u>, każde odniesienie do jego fragmentu będzie oznaczane poprzez <u>SEKCJE</u> tożsame z komentarzami zawartymi w kodzie, np. <u>Sekcja 1</u> odpowiadać będzie obszarowi przyporządkowanemu do linii kodu *# 1. Loading tools*

## Część ustawień wstępnych
Pierwsza część – **ustawienia wstępne** – odpowiada za przygotowanie programowego środowiska pomiarowego do dalszych badań. Składa się na nią m.in. załadowanie bibliotek potrzebnych w dalszych częściach programu, definicja klas oraz funkcji, odczytywanie podanych przez użytkownika parametrów badania, stworzenie miejsca zapisu danych oraz przygotowanie systemów stymulacji świetlnej i dźwiękowej. Stąd, istnieje konieczność posiadania na Raspberry następujących pakietów, wymienionych w *Sekcji 1*:
* numpy
* cv2
* math
* re
* pylab
* pygame
* io
* picamera
* RPi.GPIO
* time
* datetime
* os
* random
* sys
* xlwt

Po zadeklarowaniu bibliotek następuje część kodu, w której znajdują się ścieżki dla danych dźwiękowych, z których korzysta program oraz przełączniki programowe, dostępne w <u>Sekcji 2</u>. Można ją edytować w zależności od potrzeb, tj. zmiany ścieżek dostępu do dźwięków, jak i samej bazy IADS2 (jeśli dostępna) oraz przełączania wbudowanych w program opcji, czyli czasu rozgrzewania układu, podglądu kolejnych etapów przetwarzania każdego z zarejestrowanych zdjęć, naprawiania skalownaia wykresów zwiazanego z artefaktami pomiarowymi czy prezentacji wyników w postaci wykresów.

Dalszy kod (<u>Sekcja 3</u>) służy do odczytywania parametrów pomiaru. Ich obecność zwiazana jest z istnieniem w programie opisanych w poprzednim punkcie pięciu opcji przeprowadzania badania. W odniesieniu do wymienionej tam tabeli, przypisanie zmiennych prezentuje się następująco:</br>

<p align="center">
  <img width="700" height="150" src=Pictures\ArgumentyProgramuZmienne.JPG>
</p>

Na tym etapie program sprawdza podane przez użytkownika parametry uruchomienia pod względem poprawności (tj. ich liczby) i w przypadku podania poprawnej składni uruchomienia, przypisuje on te wartości zmiennym według zaprezentowanego powyżej klucza. W przypadku podania niepoprawnych danych, program informuje o tym użytkownika i wyłącza możliwość dalszego badania. Przypisanie wartości, znajdujące się przed częścią odczytującą parametry, jest związane z późniejszym generowaniem wykresu i powiązanymi z tym modyfikacjami zmiennych. Dodatkowo, w przypadku wybrania opcji stymulacji świetlnej, wyłączane jest usuwanie mrugnięć z wykresu (ze względu na porównywalną skalę odruchu PLR i mrugnięć podczas pomiarów źrenicy).

W <u>Sekcji 4</u>, program generuje folder do zapisu zdjęć (oraz w późniejszym czasie danych i wykresu). Nazwa folderu generowana jest w oparciu o datę badania, jego godzinę, nazwę pacjenta podaną w argumencie wywołania programu oraz typ stymulacji.

<u>Sekcja 5</u> oraz <u>Sekcja 6</u> dotyczy przygotowania systemu audio oraz świetlnego. W Raspberry Pi 3 istnieje możliwość używania kilku różnych przestrzeni nazw dla pinów GPIO, m.in. według fizycznego położenia złącza (Physical), według nazewnictwa pinów procesora (BCM) oraz według oznaczenia twórców bibliotek służących do obsługi portów. W tym projekcie, zdecydowano się na korzystanie z nazewnictwa BCM, przedstawionego poniżej.

<p align="center">
  <img width="500" height="400" src=Pictures\BCM.JPG>
</p>
Piny GPIO posiadają dwa tryby – tryb wejścia oraz tryb wyjścia. W zależności od ustawionego parametru (odpowiednio GPIO.IN i GPIO.OUT) możliwe jest odbieranie danych z zewnątrz do układu oraz wysyłanie przez port danych z układu. Należy też zwrócić uwagę na obecność drugiej diody (białej), która jest inicjowana jedynie wtedy, kiedy zostanie wybrana stymulacja świetlna (do badania PLR).

Sekcja kodu audio dotyczy trzech badań, w których używany jest system audio: ***randomsound***, ***mysound*** oraz ***startle***. Oparta jest ona o możliwości przetwarzania audio, oferowane przez bibliotekę pyGame. Mimo, iż sama biblioteka ma odmienne zastosowanie (głównie tworzenie gier), to zawarte w niej funkcje obsługi audio okazały się kluczowe z punktu widzenia działania programu – odtwarzany dźwięk nie zatrzymuje jego działania (dźwięk odtwarza się w tle podczas wykonywania dalszej części kodu), dzięki czemu możliwe jest stosowanie poleceń kontrolujących działanie kamery (których charakter obsługi powoduje zatrzymanie dalszego wykonywania kodu do momentu zakończenia rejestracji wideo).
Mimo to, że wszystkie wymienione powyżej badania opierają się na stymulacji audio, każda z nich charakteryzuje się odrębnym protokołem ładowania dźwięków. Badanie ***randomsound*** posiada w sobie część odpowiedzialną za skanowanie folderu w poszukiwaniu plików dźwiękowych oraz część zajmującą się losowym wyborem ścieżki dźwiękowej stosowanej do stymulacji. Skanowanie folderów obecne jest również w części ustawień programu ***mysound***, lecz pełni tam rolę wyłącznie zabezpieczającą przed próbą wyboru nieistniejącego pliku audio. Oba badania ładują także do pamięci plik dźwiękowy odpowiedzialny za biały szum stosowany przed badaniem. Plik ten został wygenerowany za pomocą narzędzia Audacity. Podobnie jak w przypadku mysound oraz skanowania folderów, podczas ładowania plików dla stymulacji ***startle***, wykorzystywana jest losowość, jednak w tym wypadku dotyczy ona doboru opóźnienia stymulacji, co wprowadza element nieprzewidywalności, potęgując przy tym reakcję badanego. W ostatnich liniach kodu ładowany jest wybrany przez konkretną stymulację plik oraz obliczana jest jego długość na potrzeby tworzenia wykresu.
Warto również wspomnieć o możliwości synchronizacji układu z zewnętrznymi źródłami stymulacji. Może odbywać się ona poprzez wykorzystanie programu ***light***, który powoduje pojawienie się napięcia 3,3V na pinie 23 (według notacji BCM) w momencie rozpoczęcia badania. Ta prawidłowość może być sygnałem synchronizacyjnym dla innych urządzeń oferujących taką funkcjonalność.

## Część rejestracji ze stymulacją
Druga część – **rejestracji ze stymulacją** – jest właściwą częścią pomiarową programu. Jej zadaniem jest komunikacja z kamerą celem zapisu nagrania obszaru oka oraz odpowiednia synchronizacja wybranego bodźca.

Priorytetem <u>Sekcji 7</u> i <u>Sekcji 8</u> było zapewnienie szybkiego pomiaru, przy zachowaniu jak najlepszej możliwej rozdzielczości i poprawności badania. Standardowa procedura rejestracji obrazów w formacie JPEG przy rozdzielczościach powyżej 800px x 600px może powodować problemy przy utrzymaniu szybkości 30 klatek na sekundę ze względu na szybkie wyczerpanie pamięci cache dysku. Z tego też powodu, zdecydowano się skorzystać z zaproponowanego w dokumentacji PiCamery rozwiązania polegającego na rejestracji nagrania video (przy wykorzystaniu bardziej efektywnego formatu H.264) oraz późniejszym dekodowaniu poszczególnych klatek i ich zapisie do katalogu (klasa *SplitFrames()*). Taki zabieg pozwolił na zachowanie prędkości rejestracji w okolicach 60 klatek na sekundę przy rozdzielczości 1280px x 720px. Dodatkowo, dokładność pomiaru zwiększona została poprzez samą budowę okularów pomiarowych – moduł kamery umieszczony jest stosunkowo blisko oka (około 4cm), przez co większość obszaru rejestracji zajmuje interesujący z punktu widzenia tego badania obszar. Po zakończeniu rejestracji obliczana jest również jej szybkość, celem ustalenia poprawności wykonanego badania oraz dalszych obliczeń. Dla ułatwienia, zamieszczono poniżej schemat kolejności poszczególnych procedur.

<p align="center">
  <img width="500" height="400" src=Pictures\RejestracjaProcedury.JPG>
</p>

## Część obróbki i pomiarów
Trzecia część – **obróbki oraz pomiaró**w – jest częścią odpowiadającą za polepszanie parametrów obrazów oka zarejestrowanych w poprzednim etapie, wykrycie obszaru źrenicy oraz pomiar jej średnicy.

Część ta rozpoczyna się <u>Sekcją 9</u>, w której następuje zdefiniowanie zmiennych oraz progu wykrywania źrenicy (ustawionej - zgodnie z danymi literaturowymi - w zakresie od 2 mm do 8 mm). Następnie, w <u>Sekcji 10</u>, następuje przeszukanie katalogu z zarejestrowanymi w poprzedniej części zdjęciami oraz posortowaniu ich w kolejności wykonania. Po stworzeniu spisu zdjęć, program przechodzi do ich przetwarzania celem wykrycia źrenicy (<u>Sekcja 11</u>). W celu realizacji tego punktu przetestowano działanie dwóch różnych podejść: wykrywania okręgów na obrazie z wykorzystaniem transformacji Hougha (obecnej w bibliotece openCV2) oraz poprzez takie dobranie parametrów binaryzacji, by na zdjęciu został tylko obszar źrenicy. Pierwsze podejście, mimo prostszej implementacji, zostało odrzucone ze względu na brak powtarzalności wyników – okrąg wpisywany w obszar źrenicy był w większości sytuacji dobierany nieprawidłowo, a dodatkowo zdarzały się sytuacje wykrycia okręgów w górnych obszarach obrazu u osób posiadających makijaż oczu bądź naturalnie grubsze rzęsy. Problem mógł zostać częściowo wyeliminowany poprzez manipulacje parametrami wywoływania funkcji, lecz i w takim wypadku zdarzały się nieprawidłowości w wykrywaniu źrenicy, a na dodatek parametry musiały być powtórnie modyfikowane dla każdej badanej osoby. Graficzne ukazanie najczęstszych przypadków rejestracji przy wykorzystaniu transformacji Hougha zaprezentowano poniżej.</br></br>

<p align="center">
  <img width="500" height="400" src=Pictures\Hough.JPG>
</p></br>

W związku z powyższym, zdecydowano się na drugie podejście w wykrywaniu rozmiaru źrenicy (<u>Sekcja 11</u>). W pierwszej kolejności, obraz jest wczytywany przy jednoczesnej konwersji do skali szarości. Następnie wykonywane jest odwrotne progowanie obrazu. Po prawidłowo wykonanym progowaniu, następuje usunięcie odbitego od oka światła z diody za pomocą operacji Flood Fill od punktu o współrzędnych (0, 0). Obraz taki jest następnie łączony z obrazem pierwotnym (po wstępnej binaryzacji), dzięki czemu uzyskiwany jest obraz finalny, na którym znajduje się jedynie wykryta źrenica. Przykładową drogę powyższego algorytmu na rzeczywistym przykładzie została pokazana na schemacie ogólnego algorytmu programu.

Po wykonaniu operacji na obrazie, obliczana jest ilość białych pikseli (będąca polem obszaru źrenicy), która służy następnie wyznaczeniu jej średnicy z wykorzystaniem wzoru na pole koła. Średnia wartość 73 pikseli / 1 milimetr wyznaczona została eksperymentalnie jako średnia z 10 pomiarów powierzchni naklejki (w postaci czarnego kwadratu), umieszczonej na zamkniętej powiece.

W dalszej części sprawdzane jest, czy pomiar źrenicy mieści się w założonych literaturowo granicach, co jest sygnalizowane pojawieniem się stosownej adnotacji przy pomiarze w trybie konsolowym. Dodatkowo, podobnie jak w przypadku części rejestrującej, obliczany jest także czas działania sekcji programu. Po zakończeniu tej części, w oknie konsoli powinno pojawić się podsumowanie ilości domniemanie dobrych oraz złych pomiarów.
W programie pozostawiono również możliwość włączenia podglądu kolejnych etapów przetwarzania obrazów poprzez zmianę wartości zmiennej debugSwitch na 1. Przełączanie pomiędzy kolejnymi obrazami odbywa się wtedy poprzez wciśnięcie dowolnego klawisza na klawiaturze

## Część prezentacji i zapisu
Czwarta część – **prezentacji oraz zapisu** – odpowiada za prezentację wyników pomiarów, szkicowanie wykresu oraz zapis danych do pliku zewnętrznego. 

Ze względu na dalsze operacje na zebranych danych, w pierwszej kolejności dokonywany jest zapis do zewnętrznego pliku umożliwiający pracę nad danymi w innych programach (<u>Sekcja 13</u>). Ze względu na dalsze operacje na zebranych danych, w pierwszej kolejności dokonywany jest zapis do zewnętrznego pliku umożliwiający pracę nad danymi w innych programach. W tym celu tworzony jest arkusz, do którego pierwszych siedmiu wierszy zapisywane są kolejno: ścieżka wykonanych zdjęć, data badania, nazwa badanego, typ stymulacji oraz poszczególne czasy każdego z etapów rejestracji. Dalsze wiersza zawierają już konkretne dane pomiarowe powiązane z konkretnym momentem czasowym stymulacji. Całość zapisywana jest jako plik Pomiary.xls w katalogu z wykonanymi zdjęciami. 

W dalszym kroku wyświetlane jest podsumowanie całego badania, zawierające m.in. wyżej wymienione dane oraz dodatkowo ilość zarejestrowanych klatek, szybkość ich rejestracji i czas wykonywania obliczeń średnicy źrenicy (<u>Sekcja 14</u>).

Ostatnim krokiem wykonawczym programu jest wygenerowanie wykresu (<u>Sekcja 15</u>). Oprócz rysowania zmian średnicy źrenicy w czasie, program nakreśla także ważne z punktu widzenia badania momenty, tj. kolejno rozpoczęcie stymulacji oraz jej zakończenie. 
Dla stymulacji dźwiękowych, w których wykorzystywany jest biały szum, dodatkowo zaznaczany jest moment jego rozpoczęcia – wtedy kolejność nakreślanych momentów wygląda następująco: rozpoczęcie białego szumu, rozpoczęcie stymulacji oraz zakończenie stymulacji.
Ze względu na problem, który pojawił się podczas dłuższych badań, czyli mimowolne mrugnięcia oka, wprowadzono także mechanizm pozwalający częściowo usunąć je z prezentowanych wykresów pod nazwą *blinkRepair*, który na podstawie średniego rozmiaru źrenicy usuwa ze zbioru danych te punkty, które znacznie odbiegają od zakładanych wyników. Poprawia to wygląd informacji prezentowanych na wykresie, który dynamicznie dostosowuje zakresy osi. Opcja ta może zostać wyłączona poprzez zmianę parametru blinkRepairSwitch w kodzie programu na wartość 0. Domyślnie, opcja ta wyłącza się również dla badania light z racji podobnego z punktu widzenia programu, charakteru zmiany pod wpływem impulsu światła w porównaniu do zmiany spowodowanej mrugnięciem oka. Poprzednio opisana sekcja transportu danych do pliku zewnętrznego jest również pozbawiona efektu działania powyższego skryptu. Porównanie efektu działania opisanego tu kodu zostało zaprezentowane poniżej (przed i po). Warto zwrócić uwagę na skalę osi Y – wyeliminowanie większości danych powstałych wskutek mrugnięcia, co pozwoliło na zmniejszenie jej zakresu z 0,0 – 5,0 na zakres 3,5 – 5,0. </br></br>

<p align="center">
  <img width="700" height="300" src=Pictures\BlinkRepair.jpg>
</p></br>

# Przykładowe badania
W celu sprawdzenia poprawności działania układu, wykonano próbne pomiary dla najważniejszych z punktu widzenia urządzenia opcji. Wszystkie z nich zostały przeprowadzone zgodnie z protokołem zaprezentowanym w punkcie "[Przeprowadzanie procedury pomiaru ze stymulacją](#przeprowadzanie-procedury-pomiaru-ze-stymulacją)". 

**Pierwsza** z nich dotyczyła rejestracji statycznej oka bez zadawania stymulacji. W tym celu przeprowadzono badanie przy użyciu funkcji programu nostimulation z czasem 5 sekund. Wynik badania zaprezentowano poniżej.

<p align="center">
  <img width="600" height="400" src=Pictures\Badanie1.jpg>
</p></br>

Średni wynik rozmiaru źrenicy powyższej próby wynosił 5,88 mm przy odchyleniu standardowym 0,01 mm. Niewielkie fluktuacje źrenicy, obecne przy tym typie badań mogą być dowodem na poprawność działania układu; w momencie braku obecności bodźca, rejestrowany sygnał, zgodnie z przewidywaniami literaturowymi nie wykazuje znacznych odchyleń. 

**Drugim** badaniem kontrolnym przeprowadzonym w ramach tej pracy, jest reakcja PLR na jednosekundowy błysk światła, poprzez wykorzystanie opcji programu light. Badanie to polegało na rejestracji średnicy źrenicy w schemacie: 1s rejestracji przed bodźcem, 
1s działania bodźca oraz 5s rejestracji po ustaniu bodźca, dla jednego badanego. 
Wynik został przedstawiony poniżej.

<p align="center">
  <img width="600" height="400" src=Pictures\Badanie2.jpg>
</p></br>

Powyższa reakcja PLR – zgodna z przewidywaniami oraz innymi przykładowymi pomiarami - wskazuje na poprawność działania algorytmu mierzącego zmiany powierzchni źrenicy. Również opóźnienie reakcji na światło (wynoszące w tym wypadku około 230ms) tożsame jest z danymi obecnymi w literaturze (przykładowo 241ms), co może potwierdzać wystarczającą z punktu widzenia pupilometrii częstotliwość rejestracji oraz poprawność rejestracji zmian średnicy źrenicy w czasie. Należy jednak wspomnieć o możliwości zaistnienia problemów z rejestracją zbyt dużego zwężenia źrenicy, która jest związana z działaniem algorytmu usuwającego odbicie diody od powierzchni oka.

**Trzecie** badanie polegało na próbie potwierdzenia możliwości rejestracji zmian źrenicy na efekty emocjonalne - w tym wypadku krótkotrwały, głośny i zarazem przeraźliwy dźwięk - przy wykorzystaniu funkcji programu startle. Przykładowy wynik takiego badania zaprezentowany został poniżej.

<p align="center">
  <img width="600" height="400" src=Pictures\Badanie3.jpg>
</p></br>

Jak można zauważyć, pomimo małej skali zmian rozmiaru źrenicy, potwierdzono zdolność układu do rejestracji pupilometrycznych efektów związanych z reakcjami emocjonalnymi. Maksimum wartości pomiarowej wyniosło w tym wypadku 6,09 mm przy średniej wartości średnicy źrenicy przed pojawieniem się bodźca wynoszącej 5,95 mm. Należy jednak odnotować, że uzyskano jedynie 2,3% zmianę przy doborze bodźca zaprojektowanego na wywołanie gwałtownej i silnej reakcji emocjonalnej, co jest efektem stosunkowo małym w porównaniu do innych stymulacji, np. PLR i zmianie 71,7% (dla poprzedniego badania).

W **czwartym** przykładowym badaniu, wykorzystano standaryzowaną bazę pomiarową IADS2 w celu sprawdzenia możliwości pomiaru bardziej subtelnych efektów emocjonalnych. 
Do celów badawczych, wybrany został dźwięk nr 815 o tytule *RockNRoll* – posiada on jedne z najwyższych zmierzonych w całej bazie współczynników przyjemności, pobudzenia oraz dominacji dla obu płci, stąd efekt jego działania powinien być najbardziej widoczny. Dodatkowo, dla wyeliminowania efektu związanego z nagłym pojawieniem się dźwięku, przed badaniem odtworzone zostało nagranie zawierające biały szum o długości 4 sekund. Przykładowy wynik tego badania zaprezentowano poniżej.

<p align="center">
  <img width="600" height="400" src=Pictures\Badanie4.jpg>
</p></br>

Przykład ten jednoznacznie pokazuje trudność z rejestracją subtelniejszych reakcji emocjonalnych. Na podstawie powyższego przypadku, ciężko jest jednoznacznie określić efekt działania dźwięku stymulacyjnego na zachowanie źrenicy, a zarejestrowane zmiany – interpretując je bez kontekstu badania – mogą zostać mylnie uzasadnione spontanicznymi reakcjami źrenicy, obecnymi chociażby na wykresie badania pierwszego. 

Oprócz powyższych badań, zmierzono również **różnicę szybkości działania programu w zależności od wybranej platformy**. 
Do porównania wybrano dwa układy: <u>Raspberry Pi 3B</u> oraz <u>Raspberry Pi Zero WH</u>. 
Badanie dotyczyło dwóch kluczowych z punktu widzenia działania całego układu kwestii – **możliwości utrzymania stałej szybkości rejestracji obrazu** oraz **szybkości pomiarów źrenicy**. Metodyka dla powyższych badań była następująca: za pomocą opcji programu nostimulation, przeprowadzono serię pomiarów, manipulując przy tym czasem rejestracji w granicach 
od 1s do 14s z krokiem 1s (rozpiętość czasowa wybrana na podstawie najczęstszych czasów rejestracji, uwzględniając możliwość wstrzymania się badanego od mrugania). 
Po zakończonym pomiarze zapisywano w tabeli średnią liczbę klatek na sekundę oraz czas działania sekcji pomiarowej. Dla zmniejszenia wpływu zjawiska *throttlingu termalnego* (zmniejszania szybkości działania układu przy wysokich temperaturach w celu zapobiegania jego uszkodzenia) pomiędzy każdym pomiarem zachowywano 3 minuty przerwy. Na czas działania obydwu programów uruchomiona była także usługa zdalnego podglądu obrazu VNC, mogąca wpłynąć negatywnie na uzyskiwane wartości. Wyniki powyższych pomiarów przedstawiono poniżej.

<p align="center">
  <img width="600" height="300" src=Pictures\SzybkosciRaspberry.JPG>
</p>

Wykresy szybkości rejestracji w zależności od jej czasu prezentują się następująco:

<p align="center">
  <img width="800" height="500" src=Pictures\SzybkoscRejestracji.JPG>
</p>

Jak można zauważyć, bez względu na łączny czas badania, nie następuje żaden wyraźny spadek szybkości rejestracji obrazu, natomiast różnica pomiędzy średnią z wszystkich badań prowadzonych na Raspberry Pi 3B a Raspberry Pi Zero WH jest znikoma (kolejno 58kl/s oraz 57,5kl/s). Fakt rejestracji wolniejszej, niż wynikałoby to z zadanego w kodzie programu parametru może wynikać z losowych opóźnień w działaniu układów, sposobie działania kamery PiCamera bądź niedokładności funkcji odpowiedzialnej za zapisywanie czasu. Efekt ten został uwzględniony w kluczowych częściach programu, np. podczas rysowania wykresu oraz eksportowania danych czasowych do pliku zewnętrznego. Należy wspomnieć również o problemie, który stosunkowo rzadko pojawia się podczas rejestracji – przy niektórych pomiarach prędkość pomiarowa spada w okolice 50 klatek na sekundę. W przypadku zauważenia tak dużego odchylenia, pomiar należy powtórzyć.

Zdecydowanie ciekawszą zależność widać przy porównywaniu danych czasu wykonawczego części odpowiedzialnej za obliczenia:

<p align="center">
  <img width="800" height="500" src=Pictures\SzybkoscPrzetwarzania.JPG>
</p>

Pomimo niewielkiej różnicy sprzętowej pomiędzy układami, czas działania diametralnie różnił się na korzyść wybranego w tej pracy układ. Różnica ta zwiększała się stopniowo w zależności od czasu trwania całego badania. Dodatkowo, podczas korzystania z wersji Raspberry Pi Zero WH można było zauważyć zdecydowanie wolniejsze działanie we wszystkich czynnościach na niej wykonywanych oraz ciągłe użycie procesora na poziomie 100% (przy średnio 40% na szybszym odpowiedniku), co pozwala podejrzewać, że głównym winnym tego stanu rzeczy jest zabezpieczenie termalne procesora, zmniejszające jego prędkość przy osiągnięciu granicznych dla układu temperatur. Z tego też powodu, naturalna wydała się rezygnacja z tego układu na rzecz Raspberry Pi 3B, nawet pomimo jego większych rozmiarów.
