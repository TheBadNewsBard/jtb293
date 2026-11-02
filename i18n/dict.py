# en | es | fr | th   — {n} placeholders are numbers / dates kept from the English string
R = r"""
Alliance board|Panel de la alianza|Tableau de l'alliance|บอร์ดพันธมิตร
Command board|Panel de mando|Tableau de commandement|บอร์ดบัญชาการ
snapshot {0}|captura del {0}|relevé du {0}|ข้อมูล ณ {0}
Overview|Resumen|Aperçu|ภาพรวม
Roster|Plantilla|Effectif|รายชื่อ
Canyon|Cañón|Canyon|แคนยอน
Trends|Tendencias|Tendances|แนวโน้ม
Champion Duel|Duelo de Campeones|Duel des champions|ดวลแชมเปี้ยน
Alliances|Alianzas|Alliances|พันธมิตร
Rivals|Rivales|Rivaux|คู่แข่ง
Rules|Reglas|Règles|กติกา
Board API unreachable|API del panel inaccesible|API du tableau injoignable|เชื่อมต่อ API ของบอร์ดไม่ได้
Members|Miembros|Membres|สมาชิก
{0} since {1}|{0} desde {1}|{0} depuis le {1}|{0} ตั้งแต่ {1}
({0}) since {1}|({0}) desde {1}|({0}) depuis le {1}|({0}) ตั้งแต่ {1}
Alliance arena power|Poder de arena de la alianza|Puissance d'arène de l'alliance|พลังอารีน่าของพันธมิตร
first arena snapshot|primera captura de arena|premier relevé d'arène|ข้อมูลอารีน่าครั้งแรก
Alliance H+V|H+V de la alianza|H+V de l'alliance|H+V ของพันธมิตร
Canyon starters gap|Diferencia entre titulares del Cañón|Écart entre titulaires du Canyon|ส่วนต่างตัวจริงแคนยอน
Team {0} ahead by {1}|Equipo {0} adelante por {1}|Équipe {0} devant de {1}|ทีม {0} นำอยู่ {1}
Leadership|Liderazgo|Direction|ผู้นำ
R5 and R4s, strongest first|R5 y R4, de más fuerte a más débil|R5 et R4, du plus fort au plus faible|R5 และ R4 เรียงจากแข็งแกร่งที่สุด
click for details|clic para ver detalles|cliquer pour les détails|คลิกเพื่อดูรายละเอียด
{0} Arena|{0} arena|{0} arène|อารีน่า {0}
{0} arena|{0} arena|{0} arène|อารีน่า {0}
Warlord|Señor de la guerra|Seigneur de guerre|ขุนศึก
Muse|Musa|Muse|มิวส์
Butler|Mayordomo|Majordome|พ่อบ้าน
Recruiter|Reclutador|Recruteur|ผู้คัดเลือก
Top {0} by arena power|Top {0} por poder de arena|Top {0} par puissance d'arène|{0} อันดับแรกตามพลังอารีน่า
Top {0} members by arena power|Top {0} miembros por poder de arena|Top {0} des membres par puissance d'arène|สมาชิก {0} อันดับแรกตามพลังอารีน่า
Top {0} by hero + vehicle|Top {0} por héroe + vehículo|Top {0} par héros + véhicule|{0} อันดับแรกตามฮีโร่ + ยานพาหนะ
Top {0} members by hero + vehicle|Top {0} miembros por héroe + vehículo|Top {0} des membres par héros + véhicule|สมาชิก {0} อันดับแรกตามฮีโร่ + ยานพาหนะ
the strength measure JTB plans on|la medida de fuerza que usa JTB para planificar|la mesure de force sur laquelle JTB se base|ตัววัดความแข็งแกร่งที่ JTB ใช้วางแผน
Arena power|Poder de arena|Puissance d'arène|พลังอารีน่า
arena power|poder de arena|puissance d'arène|พลังอารีน่า
Where alliance power sits|Dónde está el poder de la alianza|Répartition de la puissance de l'alliance|พลังของพันธมิตรอยู่ตรงไหน
Troops|Tropas|Troupes|กองทหาร
Structure|Estructuras|Bâtiments|สิ่งก่อสร้าง
Hero|Héroe|Héros|ฮีโร่
Tech|Tecnología|Technologie|เทคโนโลยี
Vehicle|Vehículo|Véhicule|ยานพาหนะ
Science|Ciencia|Science|วิทยาศาสตร์
Kills|Bajas|Éliminations|การสังหาร
Total|Total|Total|รวม
Total {0}|Total {0}|Total {0}|รวม {0}
H+V is {0} of it|H+V es el {0}|H+V en représente {0}|H+V คิดเป็น {0}
Alliance strength over snapshots|Fuerza de la alianza por captura|Force de l'alliance au fil des relevés|ความแข็งแกร่งของพันธมิตรตามช่วงข้อมูล
hero + vehicle|héroe + vehículo|héros + véhicule|ฮีโร่ + ยานพาหนะ
Hero + vehicle|Héroe + vehículo|Héros + véhicule|ฮีโร่ + ยานพาหนะ
Hero + Vehicle|Héroe + Vehículo|Héros + Véhicule|ฮีโร่ + ยานพาหนะ
hero plus vehicle|héroe más vehículo|héros plus véhicule|ฮีโร่บวกยานพาหนะ
the only measure with history before {0}|la única medida con historial antes del {0}|la seule mesure avec un historique avant le {0}|ตัววัดเดียวที่มีประวัติก่อน {0}
Movers since {0}|Cambios desde {0}|Évolutions depuis le {0}|ผู้เปลี่ยนแปลงตั้งแต่ {0}
Data: JTB {0} Power Tracker, snapshot {1} ({2} members, {3} snapshots since {4}). Ranking and the Canyon balance use arena power, the measure set in Canyon Teams C9; growth charts stay on hero + vehicle, the only measure with history before {5}. Open any member to set availability (alliance passcode) or a slot (officer passcode); changes reach the Canyon Teams sheet within a minute. Avatars are rank shields standing in for in-game portraits.|Datos: JTB {0} Power Tracker, captura del {1} ({2} miembros, {3} capturas desde {4}). La clasificación y el equilibrio del Cañón usan el poder de arena, la medida fijada en Canyon Teams C9; los gráficos de crecimiento siguen con héroe + vehículo, la única medida con historial antes del {5}. Abre cualquier miembro para fijar su disponibilidad (código de la alianza) o un puesto (código de oficial); los cambios llegan a la hoja Canyon Teams en menos de un minuto. Los avatares son escudos de rango en lugar de los retratos del juego.|Données : JTB {0} Power Tracker, relevé du {1} ({2} membres, {3} relevés depuis le {4}). Le classement et l'équilibre du Canyon utilisent la puissance d'arène, la mesure définie dans Canyon Teams C9 ; les courbes de progression restent sur héros + véhicule, la seule mesure avec un historique avant le {5}. Ouvrez un membre pour régler sa disponibilité (code de l'alliance) ou une place (code d'officier) ; les changements arrivent dans la feuille Canyon Teams en moins d'une minute. Les avatars sont des blasons de rang à la place des portraits du jeu.|ข้อมูล: JTB {0} Power Tracker ข้อมูล ณ {1} (สมาชิก {2} คน, {3} ช่วงข้อมูลตั้งแต่ {4}) การจัดอันดับและการจัดสมดุลแคนยอนใช้พลังอารีน่า ซึ่งเป็นตัววัดที่ตั้งไว้ใน Canyon Teams C9 ส่วนกราฟการเติบโตยังใช้ฮีโร่ + ยานพาหนะ ซึ่งเป็นตัววัดเดียวที่มีประวัติก่อน {5} เปิดดูสมาชิกคนใดก็ได้เพื่อตั้งค่าการว่าง (รหัสพันธมิตร) หรือตำแหน่ง (รหัสเจ้าหน้าที่) การเปลี่ยนแปลงจะไปถึงชีต Canyon Teams ภายในหนึ่งนาที รูปประจำตัวเป็นโล่ยศแทนรูปในเกม
All ranks|Todos los rangos|Tous les rangs|ทุกยศ
Copy as text|Copiar como texto|Copier en texte|คัดลอกเป็นข้อความ
{0} of {1} members|{0} de {1} miembros|{0} sur {1} membres|{0} จาก {1} คน
click a row for history|clic en una fila para ver el historial|cliquer sur une ligne pour l'historique|คลิกแถวเพื่อดูประวัติ
Member|Miembro|Membre|สมาชิก
Rank|Rango|Rang|ยศ
Arena power ▾|Poder de arena ▾|Puissance d'arène ▾|พลังอารีน่า ▾
Arena power ▴|Poder de arena ▴|Puissance d'arène ▴|พลังอารีน่า ▴
T2 Starter|Titular E2|Titulaire É2|ตัวจริง T2
T1 Starter|Titular E1|Titulaire É1|ตัวจริง T1
T1 Sub|Suplente E1|Remplaçant É1|ตัวสำรอง T1
T2 Sub|Suplente E2|Remplaçant É2|ตัวสำรอง T2
Not available|No disponible|Indisponible|ไม่ว่าง
Bench|Banquillo|Banc|ม้านั่งสำรอง
new|nuevo|nouveau|ใหม่
Starters balance|Equilibrio de titulares|Équilibre des titulaires|สมดุลตัวจริง
arena power of the top {0} starters per team; subs never count|poder de arena de los {0} mejores titulares por equipo; los suplentes no cuentan|puissance d'arène des {0} meilleurs titulaires par équipe ; les remplaçants ne comptent pas|พลังอารีน่าของตัวจริง {0} อันดับแรกต่อทีม ไม่นับตัวสำรอง
Team {0}|Equipo {0}|Équipe {0}|ทีม {0}
TEAM {0}|EQUIPO {0}|ÉQUIPE {0}|ทีม {0}
Availability|Disponibilidad|Disponibilité|การว่าง
{0} members|{0} miembros|{0} membres|{0} คน
{0} only|solo {0}|{0} uniquement|เฉพาะ {0}
Both|Ambos|Les deux|ทั้งสอง
N/A|N/D|N/D|ไม่ร่วม
No vote|Sin voto|Pas de vote|ยังไม่โหวต
no vote|sin voto|pas de vote|ยังไม่โหวต
Lock in results…|Registrar resultados…|Valider les résultats…|บันทึกผล…
After Friday's Canyon: mark who showed and record the results.|Después del Cañón del viernes: marca quién se presentó y anota los resultados.|Après le Canyon du vendredi : indiquez qui était présent et notez les résultats.|หลังแคนยอนวันศุกร์: ทำเครื่องหมายว่าใครมาและบันทึกผล
After Friday's Canyon: mark who showed, enter the results and lock it into the ledger.|Después del Cañón del viernes: marca quién se presentó, anota los resultados y regístralo en el historial.|Après le Canyon du vendredi : indiquez qui était présent, saisissez les résultats et validez-les dans le registre.|หลังแคนยอนวันศุกร์: ทำเครื่องหมายว่าใครมา ใส่ผล แล้วบันทึกลงสมุดบันทึก
Clear all votes…|Borrar todos los votos…|Effacer tous les votes…|ล้างโหวตทั้งหมด…
Start a new week's poll: everyone goes back to No vote.|Empieza la encuesta de la nueva semana: todos vuelven a Sin voto.|Lancer le sondage de la semaine : tout le monde revient à Pas de vote.|เริ่มโพลสัปดาห์ใหม่: ทุกคนกลับไปเป็นยังไม่โหวต
{0} session|sesión de las {0}|session de {0}|รอบ {0}
Starters Arena|Arena de titulares|Arène des titulaires|อารีน่าตัวจริง
{0}/{1} starters|{0}/{1} titulares|{0}/{1} titulaires|ตัวจริง {0}/{1}
{0}/{1} subs|{0}/{1} suplentes|{0}/{1} remplaçants|ตัวสำรอง {0}/{1}
avg starter {0}|media por titular {0}|moyenne par titulaire {0}|เฉลี่ยต่อตัวจริง {0}
Copy lineup|Copiar alineación|Copier la composition|คัดลอกรายชื่อทีม
Starters|Titulares|Titulaires|ตัวจริง
Substitutes|Suplentes|Remplaçants|ตัวสำรอง
No vote yet|Aún sin voto|Pas encore voté|ยังไม่ได้โหวต
strongest first; each one voting {0} or Both would take a Team {1} starter spot|de más fuerte a más débil; cada uno que vote {0} o Ambos ocuparía un puesto de titular del Equipo {1}|du plus fort au plus faible ; chacun votant {0} ou Les deux prendrait une place de titulaire de l'Équipe {1}|เรียงจากแข็งแกร่งที่สุด ทุกคนที่โหวต {0} หรือทั้งสอง จะได้ตำแหน่งตัวจริงทีม {1}
Copy names|Copiar nombres|Copier les noms|คัดลอกชื่อ
Copy poll reminder|Copiar recordatorio de encuesta|Copier le rappel du sondage|คัดลอกข้อความเตือนโพล
Power trends|Tendencias de poder|Tendances de puissance|แนวโน้มพลัง
Canyon trends|Tendencias del Cañón|Tendances du Canyon|แนวโน้มแคนยอน
Track|Seguir|Suivre|ติดตาม
pick one or combine|elige uno o combina|choisir un ou combiner|เลือกหนึ่งหรือรวมกัน
applies to every chart on this tab|se aplica a todos los gráficos de esta pestaña|s'applique à tous les graphiques de cet onglet|ใช้กับทุกกราฟในแท็บนี้
Arena|Arena|Arène|อารีน่า
combine into one line|combinar en una línea|combiner en une seule courbe|รวมเป็นเส้นเดียว
show all players in gains / declines|mostrar todos los jugadores en subidas / bajadas|afficher tous les joueurs dans hausses / baisses|แสดงผู้เล่นทั้งหมดในส่วนเพิ่มขึ้น / ลดลง
From|Desde|Du|จาก
{0} (first)|{0} (primera)|{0} (premier)|{0} (ครั้งแรก)
to {0}|al {0}|au {0}|ถึง {0}
{0} to {1}|{0} al {1}|du {0} au {1}|{0} ถึง {1}
Alliance {0}|Alianza {0}|Alliance {0}|พันธมิตร {0}
Total change since {0}|Cambio total desde {0}|Variation totale depuis le {0}|การเปลี่ยนแปลงรวมตั้งแต่ {0}
over {0} days|en {0} días|sur {0} jours|ใน {0} วัน
over {0} day|en {0} día|sur {0} jour|ใน {0} วัน
Same members (in both snapshots|Mismos miembros (en ambas capturas|Mêmes membres (dans les deux relevés|สมาชิกเดิม (อยู่ในทั้งสองช่วงข้อมูล
{0})|{0})|{0})|{0})
avg {0} each|media de {0} cada uno|moyenne {0} chacun|เฉลี่ยคนละ {0}
Roster turnover|Rotación de la plantilla|Renouvellement de l'effectif|การเปลี่ยนแปลงรายชื่อ
{0} → {1} members|{0} → {1} miembros|{0} → {1} membres|{0} → {1} คน
joined {0}, left {1}|entraron {0}, salieron {1}|arrivés {0}, partis {1}|เข้า {0} ออก {1}
net {0}|neto {0}|net {0}|สุทธิ {0}
All gains since {0}|Todas las subidas desde {0}|Toutes les hausses depuis le {0}|การเพิ่มขึ้นทั้งหมดตั้งแต่ {0}
All declines since {0}|Todas las bajadas desde {0}|Toutes les baisses depuis le {0}|การลดลงทั้งหมดตั้งแต่ {0}
Biggest gains since {0}|Mayores subidas desde {0}|Plus fortes hausses depuis le {0}|เพิ่มขึ้นมากที่สุดตั้งแต่ {0}
Declines since {0}|Bajadas desde {0}|Baisses depuis le {0}|ลดลงตั้งแต่ {0}
{0} of {1}|{0} de {1}|{0} sur {1}|{0} จาก {1}
Nobody lost power on this measure.|Nadie perdió poder en esta medida.|Personne n'a perdu de puissance sur cette mesure.|ไม่มีใครเสียพลังในตัววัดนี้
No gains recorded.|No hay subidas registradas.|Aucune hausse enregistrée.|ไม่มีการเพิ่มขึ้นที่บันทึกไว้
Only one snapshot has this measure so far.|Por ahora solo una captura tiene esta medida.|Un seul relevé contient cette mesure pour l'instant.|ตอนนี้มีข้อมูลตัววัดนี้เพียงช่วงเดียว
Joined since {0}|Entraron desde {0}|Arrivés depuis le {0}|เข้าร่วมตั้งแต่ {0}
Left since {0}|Salieron desde {0}|Partis depuis le {0}|ออกไปตั้งแต่ {0}
None|Ninguno|Aucun|ไม่มี
Arena power is only recorded from {0} on, so its history starts there.|El poder de arena solo se registra desde el {0}, así que su historial empieza ahí.|La puissance d'arène n'est enregistrée qu'à partir du {0}, son historique commence donc là.|พลังอารีน่าเริ่มบันทึกตั้งแต่ {0} ประวัติจึงเริ่มจากวันนั้น
Hero + vehicle|Héroe + vehículo|Héros + véhicule|ฮีโร่ + ยานพาหนะ
Canyon Clash ledger|Historial de Canyon Clash|Registre du Canyon Clash|สมุดบันทึก Canyon Clash
{0} Fridays locked in|{0} viernes registrados|{0} vendredis validés|บันทึกแล้ว {0} วันศุกร์
{0} Friday locked in|{0} viernes registrado|{0} vendredi validé|บันทึกแล้ว {0} วันศุกร์
updated {0}|actualizado el {0}|mis à jour le {0}|อัปเดต {0}
Could not reach the board API for the ledger. Try again in a moment.|No se pudo conectar con la API del panel para el historial. Inténtalo de nuevo en un momento.|Impossible de joindre l'API du tableau pour le registre. Réessayez dans un instant.|เชื่อมต่อ API ของบอร์ดเพื่อโหลดสมุดบันทึกไม่ได้ ลองใหม่อีกครั้งในอีกสักครู่
Loading the ledger…|Cargando el historial…|Chargement du registre…|กำลังโหลดสมุดบันทึก…
No Canyon locked in yet. After Friday's Canyon, an officer opens the Canyon tab, sets each player's Show / No-show chip and presses|Aún no hay ningún Cañón registrado. Después del Cañón del viernes, un oficial abre la pestaña Cañón, marca a cada jugador como Presente / Ausente y pulsa|Aucun Canyon validé pour l'instant. Après le Canyon du vendredi, un officier ouvre l'onglet Canyon, règle chaque joueur sur Présent / Absent et appuie sur|ยังไม่มีแคนยอนที่บันทึกไว้ หลังแคนยอนวันศุกร์ เจ้าหน้าที่จะเปิดแท็บแคนยอน ตั้งค่ามา / ไม่มา ของผู้เล่นแต่ละคน แล้วกด
. The record, attendance and player stats build up here from then on.|. A partir de ahí, aquí se acumulan el récord, la asistencia y las estadísticas de los jugadores.|. Le bilan, la présence et les statistiques des joueurs s'accumulent ensuite ici.|จากนั้นสถิติผลแข่ง การเข้าร่วม และข้อมูลผู้เล่นจะสะสมอยู่ที่นี่
Both teams|Ambos equipos|Les deux équipes|ทั้งสองทีม
{0} team|equipo de las {0}|équipe de {0}|ทีม {0}
All Fridays|Todos los viernes|Tous les vendredis|ทุกวันศุกร์
all Fridays|todos los viernes|tous les vendredis|ทุกวันศุกร์
Last {0}|Últimos {0}|{0} derniers|{0} ครั้งล่าสุด
last {0}|últimos {0}|{0} derniers|{0} ครั้งล่าสุด
Starters + subs|Titulares + suplentes|Titulaires + remplaçants|ตัวจริง + ตัวสำรอง
Starters only|Solo titulares|Titulaires uniquement|เฉพาะตัวจริง
Subs only|Solo suplentes|Remplaçants uniquement|เฉพาะตัวสำรอง
Current members|Miembros actuales|Membres actuels|สมาชิกปัจจุบัน
Include members who left|Incluir miembros que se fueron|Inclure les membres partis|รวมสมาชิกที่ออกไปแล้ว
{0} Fridays|{0} viernes|{0} vendredis|{0} วันศุกร์
{0} Friday|{0} viernes|{0} vendredi|{0} วันศุกร์
{0} matches (each team plays its own opponent)|{0} partidas (cada equipo juega contra su propio rival)|{0} matchs (chaque équipe a son propre adversaire)|{0} แมตช์ (แต่ละทีมเจอคู่แข่งของตัวเอง)
{0} match (each team plays its own opponent)|{0} partida (cada equipo juega contra su propio rival)|{0} match (chaque équipe a son propre adversaire)|{0} แมตช์ (แต่ละทีมเจอคู่แข่งของตัวเอง)
Canyons played|Cañones jugados|Canyons joués|แคนยอนที่เล่นแล้ว
{0} team matches|{0} partidas por equipo|{0} matchs d'équipe|{0} แมตช์ของทีม
since {0}|desde {0}|depuis le {0}|ตั้งแต่ {0}
Record|Récord|Bilan|สถิติ
no results entered yet|aún no hay resultados|aucun résultat saisi|ยังไม่มีผลที่บันทึก
{0} win rate|{0} de victorias|{0} de victoires|อัตราชนะ {0}
Starter attendance|Asistencia de titulares|Présence des titulaires|การมาของตัวจริง
{0} of {1} starter slots showed|se presentaron {0} de {1} titulares|{0} titulaires présents sur {1}|ตัวจริงมา {0} จาก {1} ตำแหน่ง
No-shows|Ausencias|Absences|ไม่มา
{0} no-show rate|{0} de ausencias|{0} d'absences|อัตราไม่มา {0}
{0} sub fill-ins|{0} entradas de suplentes|{0} remplacements|ตัวสำรองลงแทน {0} ครั้ง
Results by Friday|Resultados por viernes|Résultats par vendredi|ผลแยกตามวันศุกร์
green win|verde victoria|vert victoire|เขียว ชนะ
red loss|rojo derrota|rouge défaite|แดง แพ้
grey no result yet|gris sin resultado|gris pas de résultat|เทา ยังไม่มีผล
hover for score and opponent|pasa el cursor para ver marcador y rival|survolez pour le score et l'adversaire|วางเมาส์เพื่อดูคะแนนและคู่แข่ง
Win rate by team|Porcentaje de victorias por equipo|Taux de victoire par équipe|อัตราชนะแยกตามทีม
Our starters vs opponent power|Nuestros titulares vs poder del rival|Nos titulaires vs puissance adverse|ตัวจริงของเราเทียบกับพลังคู่แข่ง
Stronger on paper:|Más fuertes sobre el papel:|Plus forts sur le papier :|แข็งแกร่งกว่าบนกระดาษ:
weaker:|más débiles:|plus faibles :|อ่อนกว่า:
Enter the opponent's total power when locking to see how often the stronger side won.|Introduce el poder total del rival al registrar para ver con qué frecuencia ganó el más fuerte.|Saisissez la puissance totale adverse lors de la validation pour voir à quelle fréquence le camp le plus fort a gagné.|ใส่พลังรวมของคู่แข่งตอนบันทึก เพื่อดูว่าฝ่ายที่แข็งกว่าชนะบ่อยแค่ไหน
Starter attendance per Friday|Asistencia de titulares por viernes|Présence des titulaires par vendredi|การมาของตัวจริงในแต่ละวันศุกร์
Starter attendance by Friday|Asistencia de titulares por viernes|Présence des titulaires par vendredi|การมาของตัวจริงในแต่ละวันศุกร์
share of rostered starters who showed|porcentaje de titulares convocados que se presentaron|part des titulaires inscrits qui étaient présents|สัดส่วนตัวจริงที่มา
Attendance|Asistencia|Présence|การเข้าร่วม
Most no-shows|Más ausencias|Le plus d'absences|ไม่มามากที่สุด
{0} of {1} starts|{0} de {1} titularidades|{0} sur {1} titularisations|{0} จาก {1} ครั้งที่เป็นตัวจริง
Nobody missed a start.|Nadie faltó como titular.|Personne n'a manqué une titularisation.|ไม่มีใครขาดตอนเป็นตัวจริง
Players|Jugadores|Joueurs|ผู้เล่น
played = started and showed, or a sub who played|jugó = titular que se presentó, o suplente que jugó|joué = titulaire présent, ou remplaçant qui a joué|เล่น = ตัวจริงที่มา หรือตัวสำรองที่ได้ลง
no-show rate = no-shows ÷ starts|tasa de ausencia = ausencias ÷ titularidades|taux d'absence = absences ÷ titularisations|อัตราไม่มา = ครั้งที่ไม่มา ÷ ครั้งที่เป็นตัวจริง
W–L only counts matches they played|V–D solo cuenta las partidas que jugaron|V–D ne compte que les matchs joués|ชนะ–แพ้ นับเฉพาะแมตช์ที่ได้เล่น
click a header to sort|clic en un encabezado para ordenar|cliquer sur un en-tête pour trier|คลิกหัวคอลัมน์เพื่อเรียง
Player|Jugador|Joueur|ผู้เล่น
Rostered|Convocado|Inscrit|ถูกจัดทีม
Starter|Titular|Titulaire|ตัวจริง
Sub|Suplente|Remplaçant|ตัวสำรอง
sub|suplente|remplaçant|สำรอง
Played|Jugó|Joué|ได้เล่น
No-show|Ausente|Absent|ไม่มา
No-show rate|Tasa de ausencia|Taux d'absence|อัตราไม่มา
Not needed|No necesario|Pas nécessaire|ไม่ได้ใช้
W–L|V–D|V–D|ชนะ–แพ้
Win rate|% victorias|Taux de victoire|อัตราชนะ
Avg points|Puntos medios|Points moyens|คะแนนเฉลี่ย
Recent (newest right)|Recientes (más nuevo a la derecha)|Récents (plus récent à droite)|ล่าสุด (ใหม่สุดทางขวา)
Recent|Recientes|Récents|ล่าสุด
(left)|(se fue)|(parti)|(ออกแล้ว)
also locked as|también registrado como|aussi validé sous|บันทึกในชื่ออื่นด้วย
Showed / played|Se presentó / jugó|Présent / a joué|มา / ได้เล่น
Sub, not needed|Suplente, no necesario|Remplaçant, pas nécessaire|ตัวสำรอง ไม่ได้ใช้
Fridays|Viernes|Vendredis|วันศุกร์
newest first|más reciente primero|plus récent d'abord|ใหม่สุดก่อน
each team's opponent, result and roster|rival, resultado y plantilla de cada equipo|adversaire, résultat et effectif de chaque équipe|คู่แข่ง ผล และรายชื่อของแต่ละทีม
officers can edit a Friday|los oficiales pueden editar un viernes|les officiers peuvent modifier un vendredi|เจ้าหน้าที่แก้ไขวันศุกร์ได้
{0} Win {1}–{2}|{0} Victoria {1}–{2}|{0} Victoire {1}–{2}|{0} ชนะ {1}–{2}
{0} Loss {1}–{2}|{0} Derrota {1}–{2}|{0} Défaite {1}–{2}|{0} แพ้ {1}–{2}
{0} Win|{0} Victoria|{0} Victoire|{0} ชนะ
{0} Loss|{0} Derrota|{0} Défaite|{0} แพ้
{0}/{1} starters showed|{0}/{1} titulares presentes|{0}/{1} titulaires présents|ตัวจริงมา {0}/{1}
Edit|Editar|Modifier|แก้ไข
Opponent|Rival|Adversaire|คู่แข่ง
Their power|Su poder|Leur puissance|พลังของคู่แข่ง
Our starters|Nuestros titulares|Nos titulaires|ตัวจริงของเรา
Score|Marcador|Score|คะแนน
Locked {0}|Registrado el {0}|Validé le {0}|บันทึกเมื่อ {0}
Locked {0} by|Registrado el {0} por|Validé le {0} par|บันทึกเมื่อ {0} โดย
edited {0}|editado el {0}|modifié le {0}|แก้ไขเมื่อ {0}
edited {0} by|editado el {0} por|modifié le {0} par|แก้ไขเมื่อ {0} โดย
Canyon record|Récord en el Cañón|Bilan au Canyon|สถิติแคนยอน
{0} rostered|{0} convocatorias|{0} inscriptions|ถูกจัดทีม {0} ครั้ง
Not on a locked Canyon roster yet.|Aún no está en ninguna plantilla registrada del Cañón.|Pas encore dans un effectif de Canyon validé.|ยังไม่อยู่ในรายชื่อแคนยอนที่บันทึกไว้
Starter / sub|Titular / suplente|Titulaire / remplaçant|ตัวจริง / ตัวสำรอง
({0} of starts)|({0} de titularidades)|({0} des titularisations)|({0} ของครั้งที่เป็นตัวจริง)
Champion Duel|Duelo de Campeones|Duel des champions|ดวลแชมเปี้ยน
qualifiers|clasificatorias|qualifications|รอบคัดเลือก
{0} players|{0} jugadores|{0} joueurs|ผู้เล่น {0} คน
{0} players. Lock in after Friday's matches, then clear the votes for next week.|{0} jugadores. Registra después de las partidas del viernes y luego borra los votos para la próxima semana.|{0} joueurs. Validez après les matchs du vendredi, puis effacez les votes pour la semaine suivante.|ผู้เล่น {0} คน บันทึกหลังแมตช์วันศุกร์ แล้วล้างโหวตสำหรับสัปดาห์หน้า
Last locked: {0}|Último registro: {0}|Dernière validation : {0}|บันทึกล่าสุด: {0}
Snapshot {0}|Captura {0}|Relevé {0}|ข้อมูล {0}
Snapshot|Captura|Relevé|ข้อมูล
top {0} per server, {1} server|top {0} por servidor, {1} servidor|top {0} par serveur, {1} serveur|{0} อันดับแรกต่อเซิร์ฟเวอร์, {1} เซิร์ฟเวอร์
top {0} per server, {1} servers|top {0} por servidor, {1} servidores|top {0} par serveur, {1} serveurs|{0} อันดับแรกต่อเซิร์ฟเวอร์, {1} เซิร์ฟเวอร์
All servers|Todos los servidores|Tous les serveurs|ทุกเซิร์ฟเวอร์
Server {0}|Servidor {0}|Serveur {0}|เซิร์ฟเวอร์ {0}
All alliances|Todas las alianzas|Toutes les alliances|ทุกพันธมิตร
{0} shown|{0} mostrados|{0} affichés|แสดง {0}
player power and kills as shown in the Champion Duel panel; arena 1st march from Arena 3v3, 1v1 Peak Match, our roster (JTB) or the duel; {0} marches = all three added, from 3v3 when known else the duel|poder y bajas del jugador tal como aparecen en el panel del Duelo de Campeones; arena 1.ª marcha de Arena 3v3, 1v1 Peak Match, nuestra plantilla (JTB) o el duelo; {0} marchas = las tres sumadas, de 3v3 si se conoce, si no del duelo|puissance et éliminations du joueur telles qu'affichées dans le panneau du Duel des champions ; arène 1re marche depuis Arène 3v3, 1v1 Peak Match, notre effectif (JTB) ou le duel ; {0} marches = les trois additionnées, depuis le 3v3 si connu, sinon le duel|พลังและการสังหารของผู้เล่นตามที่แสดงในหน้าดวลแชมเปี้ยน อารีน่าทัพที่ 1 มาจาก Arena 3v3, 1v1 Peak Match, รายชื่อของเรา (JTB) หรือการดวล {0} ทัพ = รวมทั้งสามทัพ จาก 3v3 ถ้ามี ไม่เช่นนั้นจากการดวล
Alliance|Alianza|Alliance|พันธมิตร
Server|Servidor|Serveur|เซิร์ฟเวอร์
Personal power|Poder personal|Puissance personnelle|พลังส่วนตัว
Arena, 1st march|Arena, 1.ª marcha|Arène, 1re marche|อารีน่า ทัพที่ 1
Arena, {0} marches|Arena, {0} marchas|Arène, {0} marches|อารีน่า {0} ทัพ
Points|Puntos|Points|คะแนน
pts|pts|pts|คะแนน
Search player or alliance|Buscar jugador o alianza|Chercher un joueur ou une alliance|ค้นหาผู้เล่นหรือพันธมิตร
Server {0} alliances by power|Alianzas del servidor {0} por poder|Alliances du serveur {0} par puissance|พันธมิตรในเซิร์ฟเวอร์ {0} ตามพลัง
Name|Nombre|Nom|ชื่อ
Power|Poder|Puissance|พลัง
Gap to JTB|Diferencia con JTB|Écart avec JTB|ส่วนต่างกับ JTB
Top-{0} entrants|Participantes en el top {0}|Participants du top {0}|ผู้เข้าแข่งใน {0} อันดับแรก
Best duel rank|Mejor puesto en el duelo|Meilleur rang au duel|อันดับดวลที่ดีที่สุด
Avg entrant personal power|Poder personal medio por participante|Puissance personnelle moyenne par participant|พลังส่วนตัวเฉลี่ยของผู้เข้าแข่ง
Entrant columns come from the server {0} Champion Duel qualifier top {1} (snapshot {2}); power ranking from the in-game alliance list.|Las columnas de participantes vienen del top {1} de la clasificatoria del Duelo de Campeones del servidor {0} (captura {2}); la clasificación de poder, de la lista de alianzas del juego.|Les colonnes des participants viennent du top {1} des qualifications du Duel des champions du serveur {0} (relevé {2}) ; le classement de puissance vient de la liste des alliances du jeu.|คอลัมน์ผู้เข้าแข่งมาจาก {1} อันดับแรกของรอบคัดเลือกดวลแชมเปี้ยนในเซิร์ฟเวอร์ {0} (ข้อมูล {2}) ส่วนอันดับพลังมาจากรายชื่อพันธมิตรในเกม
Alliance total power|Poder total de la alianza|Puissance totale de l'alliance|พลังรวมของพันธมิตร
JTB by rank|JTB por rango|JTB par rang|JTB แยกตามยศ
Group|Grupo|Groupe|กลุ่ม
Avg Arena|Arena media|Arène moyenne|อารีน่าเฉลี่ย
JTB by arena power band|JTB por franja de poder de arena|JTB par tranche de puissance d'arène|JTB แยกตามช่วงพลังอารีน่า
JTB by hero + vehicle band|JTB por franja de héroe + vehículo|JTB par tranche héros + véhicule|JTB แยกตามช่วงฮีโร่ + ยานพาหนะ
JTB by HQ level|JTB por nivel de HQ|JTB par niveau de QG|JTB แยกตามเลเวล HQ
HQ|HQ|QG|HQ
HQ {0}|HQ {0}|QG {0}|HQ {0}
JTB roster slices use the {0} snapshot. The full ranked roster and per-metric trends are on the Roster and Trends tabs.|Los desgloses de la plantilla de JTB usan la captura del {0}. La plantilla completa clasificada y las tendencias por métrica están en las pestañas Plantilla y Tendencias.|Les répartitions de l'effectif JTB utilisent le relevé du {0}. L'effectif complet classé et les tendances par mesure sont dans les onglets Effectif et Tendances.|การแบ่งกลุ่มรายชื่อ JTB ใช้ข้อมูล ณ {0} รายชื่อเต็มพร้อมอันดับและแนวโน้มแต่ละตัววัดอยู่ในแท็บรายชื่อและแนวโน้ม
arena power from Champion Duel + Arena|poder de arena del Duelo de Campeones + Arena|puissance d'arène depuis le Duel des champions + l'Arène|พลังอารีน่าจากดวลแชมเปี้ยน + อารีน่า
last capture {0}|última captura {0}|dernier relevé {0}|บันทึกล่าสุด {0}
Servers|Servidores|Serveurs|เซิร์ฟเวอร์
All sources|Todas las fuentes|Toutes les sources|ทุกแหล่งข้อมูล
Champion Duel KO|Duelo de Campeones KO|Duel des champions KO|ดวลแชมเปี้ยน KO
Arena 3v3|Arena 3v3|Arène 3v3|อารีน่า 3v3
Arena 1v1 Peak top {0}|Arena 1v1 Peak top {0}|Arène 1v1 Peak top {0}|อารีน่า 1v1 Peak {0} อันดับแรก
Other servers only|Solo otros servidores|Autres serveurs uniquement|เฉพาะเซิร์ฟเวอร์อื่น
Total arena|Arena total|Arène totale|อารีน่ารวม
{0} marches|{0} marchas|{0} marches|{0} ทัพ
1st march|1.ª marcha|1re marche|ทัพที่ 1
Duel total|Total del duelo|Total du duel|รวมการดวล
Duel marches|Marchas del duelo|Marches du duel|ทัพในการดวล
KO R1|KO R1|KO T1|KO R1
Change|Cambio|Variation|การเปลี่ยนแปลง
Duel|Duelo|Duel|ดวล
not played|no jugado|pas joué|ไม่ได้เล่น
= all three marches added together.|= las tres marchas sumadas.|= les trois marches additionnées.|= รวมทั้งสามทัพ
From 3v3|De 3v3|Depuis 3v3|จาก 3v3
= the player's own Arena 3v3 lineup (best source);|= la alineación propia del jugador en Arena 3v3 (mejor fuente);|= la composition Arène 3v3 du joueur (meilleure source) ;|= รายชื่อ Arena 3v3 ของผู้เล่นเอง (แหล่งที่ดีที่สุด)
From Duel|Del duelo|Depuis le duel|จากการดวล
= their Champion Duel Knockout marches, where weapons are spread across the three to win {0} of {1} head-to-heads.|= sus marchas de eliminatoria del Duelo de Campeones, donde las armas se reparten entre las tres para ganar {0} de {1} enfrentamientos.|= leurs marches de phase finale du Duel des champions, où les armes sont réparties sur les trois pour gagner {0} duels sur {1}.|= ทัพรอบน็อกเอาต์ของดวลแชมเปี้ยน ซึ่งกระจายอาวุธไปทั้งสามทัพเพื่อชนะ {0} จาก {1} การปะทะ
= 3v3 march {0}, else the Arena 1v1 Peak Match lineup, else duel march {1}. Players with only a 1st march have no total yet and sort to the bottom. ~ marks values the game shows only to {2}.|= marcha {0} de 3v3; si no, la alineación de Arena 1v1 Peak Match; si no, la marcha {1} del duelo. Los jugadores con solo una 1.ª marcha aún no tienen total y van al final. ~ marca valores que el juego muestra solo con precisión de {2}.|= marche {0} du 3v3, sinon la composition Arène 1v1 Peak Match, sinon la marche {1} du duel. Les joueurs n'ayant qu'une 1re marche n'ont pas encore de total et sont classés en bas. ~ marque les valeurs que le jeu n'affiche qu'à {2} près.|= ทัพที่ {0} ของ 3v3 ไม่เช่นนั้นใช้รายชื่อ Arena 1v1 Peak Match ไม่เช่นนั้นใช้ทัพที่ {1} ของการดวล ผู้เล่นที่มีเฉพาะทัพที่ 1 ยังไม่มีผลรวมและถูกเรียงไว้ท้ายสุด ~ หมายถึงค่าที่เกมแสดงละเอียดแค่ {2}
Avg total arena|Arena total media|Arène totale moyenne|อารีน่ารวมเฉลี่ย
Max total arena|Arena total máxima|Arène totale max|อารีน่ารวมสูงสุด
Sum total arena|Suma de arena total|Somme de l'arène totale|ผลรวมอารีน่ารวม
With total|Con total|Avec total|มีผลรวม
Avg 1st march|1.ª marcha media|1re marche moyenne|ทัพที่ 1 เฉลี่ย
KO R1 W–L|KO R1 V–D|KO T1 V–D|KO R1 ชนะ–แพ้
Peak top-30|Peak top 30|Peak top 30|Peak 30 อันดับแรก
Top player|Mejor jugador|Meilleur joueur|ผู้เล่นอันดับต้น
Canyon Clash rules digest|Resumen de reglas de Canyon Clash|Résumé des règles du Canyon Clash|สรุปกติกา Canyon Clash
Source: in-game Rules / Building Info / Rewards screens, read {0}.|Fuente: pantallas del juego Reglas / Info de edificios / Recompensas, leídas el {0}.|Source : écrans Règles / Infos bâtiments / Récompenses du jeu, lus le {0}.|ที่มา: หน้ากติกา / ข้อมูลอาคาร / รางวัลในเกม อ่านเมื่อ {0}
Weekly schedule|Calendario semanal|Calendrier hebdomadaire|ตารางรายสัปดาห์
Mon–Tue|Lun–Mar|Lun–Mar|จ.–อ.
Voting on the battle session (three options, e.g. {0} / {1} / {2} Apocalypse Time).|Votación de la sesión de batalla (tres opciones, p. ej. {0} / {1} / {2} hora Apocalipsis).|Vote pour la session de bataille (trois options, par ex. {0} / {1} / {2} heure Apocalypse).|โหวตรอบการต่อสู้ (สามตัวเลือก เช่น {0} / {1} / {2} เวลา Apocalypse)
Wed|Mié|Mer|พ.
Registration (R5/R4 register the alliance and pick participants).|Inscripción (R5/R4 inscriben a la alianza y eligen a los participantes).|Inscription (R5/R4 inscrivent l'alliance et choisissent les participants).|ลงทะเบียน (R5/R4 ลงทะเบียนพันธมิตรและเลือกผู้เข้าร่วม)
Thu|Jue|Jeu|พฤ.
Matchmaking.|Emparejamiento.|Appariement.|จับคู่
Fri|Vie|Ven|ศ.
Combat.|Combate.|Combat.|ต่อสู้
Eligibility|Requisitos|Éligibilité|คุณสมบัติ
Top {0} by power on the server and at least {1} members. At least {2} registered members to enter matchmaking.|Top {0} por poder en el servidor y al menos {1} miembros. Al menos {2} miembros inscritos para entrar en el emparejamiento.|Top {0} en puissance sur le serveur et au moins {1} membres. Au moins {2} membres inscrits pour entrer dans l'appariement.|อยู่ใน {0} อันดับแรกตามพลังในเซิร์ฟเวอร์และมีสมาชิกอย่างน้อย {1} คน ต้องมีสมาชิกลงทะเบียนอย่างน้อย {2} คนจึงจะเข้าจับคู่ได้
Who registers|Quién inscribe|Qui inscrit|ใครเป็นผู้ลงทะเบียน
Alliance leader (R5) and R4s.|Líder de la alianza (R5) y R4.|Chef de l'alliance (R5) et R4.|หัวหน้าพันธมิตร (R5) และ R4
Participants|Participantes|Participants|ผู้เข้าร่วม
Must have been in the alliance {0}+ hours. Offline {1}+ days = not selectable.|Debe llevar {0}+ horas en la alianza. Desconectado {1}+ días = no seleccionable.|Doit être dans l'alliance depuis {0} h ou plus. Hors ligne {1} jours ou plus = non sélectionnable.|ต้องอยู่ในพันธมิตร {0}+ ชั่วโมง ออฟไลน์ {1}+ วัน = เลือกไม่ได้
One team only|Solo un equipo|Une seule équipe|ได้ทีมเดียว
Each member can be in only one team (starter or substitute).|Cada miembro solo puede estar en un equipo (titular o suplente).|Chaque membre ne peut être que dans une équipe (titulaire ou remplaçant).|สมาชิกแต่ละคนอยู่ได้เพียงทีมเดียว (ตัวจริงหรือตัวสำรอง)
Opens {0} weeks after Canyon Clash starts. Needs ≥{1} active members AND ≥{2} members who scored {3}+ in a single battle last week. Alliance rewards depend on Team {4}'s result; Team {5} fighters still get personal and points rewards.|Se abre {0} semanas después del inicio de Canyon Clash. Requiere ≥{1} miembros activos Y ≥{2} miembros que hicieran {3}+ en una sola batalla la semana pasada. Las recompensas de alianza dependen del resultado del Equipo {4}; los del Equipo {5} siguen recibiendo recompensas personales y por puntos.|S'ouvre {0} semaines après le début du Canyon Clash. Nécessite ≥{1} membres actifs ET ≥{2} membres ayant marqué {3}+ en une seule bataille la semaine précédente. Les récompenses d'alliance dépendent du résultat de l'Équipe {4} ; les combattants de l'Équipe {5} reçoivent quand même les récompenses personnelles et de points.|เปิดหลังเริ่ม Canyon Clash {0} สัปดาห์ ต้องมีสมาชิกที่แอ็กทีฟ ≥{1} คน และสมาชิก ≥{2} คนที่ทำได้ {3}+ ในการต่อสู้ครั้งเดียวเมื่อสัปดาห์ก่อน รางวัลพันธมิตรขึ้นกับผลของทีม {4} ผู้เล่นทีม {5} ยังได้รางวัลส่วนตัวและรางวัลคะแนน
Roster limits (per team)|Límites de plantilla (por equipo)|Limites d'effectif (par équipe)|จำนวนผู้เล่นสูงสุด (ต่อทีม)
{0} – can enter during the prep phase.|{0} – pueden entrar durante la fase de preparación.|{0} – peuvent entrer pendant la phase de préparation.|{0} – เข้าได้ระหว่างช่วงเตรียมตัว
{0} – can enter when combat begins if starters are absent.|{0} – pueden entrar al empezar el combate si faltan titulares.|{0} – peuvent entrer au début du combat si des titulaires sont absents.|{0} – เข้าได้เมื่อเริ่มต่อสู้ถ้าตัวจริงไม่มา
Commanders|Comandantes|Commandants|ผู้บัญชาการ
{0} – must be a starter or substitute. Can group participants and issue commands. Set during registration; once the battlefield opens they can only be changed inside it. Only R4/R5 can assign.|{0} – deben ser titulares o suplentes. Pueden agrupar participantes y dar órdenes. Se fijan durante la inscripción; una vez abierto el campo de batalla solo se pueden cambiar dentro. Solo R4/R5 pueden asignarlos.|{0} – doivent être titulaires ou remplaçants. Peuvent regrouper les participants et donner des ordres. Définis pendant l'inscription ; une fois le champ de bataille ouvert, ils ne peuvent être changés qu'à l'intérieur. Seuls les R4/R5 peuvent les désigner.|{0} – ต้องเป็นตัวจริงหรือตัวสำรอง จัดกลุ่มผู้เข้าร่วมและสั่งการได้ ตั้งระหว่างลงทะเบียน เมื่อสนามรบเปิดแล้วเปลี่ยนได้เฉพาะในสนาม เฉพาะ R4/R5 เท่านั้นที่แต่งตั้งได้
Matchmaking|Emparejamiento|Appariement|การจับคู่
Based mainly on the highest power on record of participating members.|Basado sobre todo en el poder máximo registrado de los miembros participantes.|Basé principalement sur la puissance maximale enregistrée des membres participants.|อิงจากพลังสูงสุดที่เคยบันทึกของสมาชิกที่เข้าร่วมเป็นหลัก
Entering|Entrada|Entrée|การเข้าสนาม
All troops must be back at HQ, carrying all deployable units.|Todas las tropas deben estar de vuelta en el HQ, con todas las unidades desplegables.|Toutes les troupes doivent être revenues au QG, avec toutes les unités déployables.|ทหารทั้งหมดต้องกลับมาที่ HQ พร้อมหน่วยที่ส่งออกได้ทั้งหมด
Battle flow|Desarrollo de la batalla|Déroulement de la bataille|ลำดับการต่อสู้
Prep phase|Fase de preparación|Phase de préparation|ช่วงเตรียมตัว
Starters enter and wait.|Los titulares entran y esperan.|Les titulaires entrent et attendent.|ตัวจริงเข้าและรอ
Phase I|Fase I|Phase I|ช่วงที่ I
Field Hospital and Water Refinery open (buffs + points). Quarry gives extra personal points.|Se abren el Hospital de campaña y la Refinería de agua (bonificaciones + puntos). La Cantera da puntos personales extra.|L'Hôpital de campagne et la Raffinerie d'eau ouvrent (bonus + points). La Carrière donne des points personnels en plus.|โรงพยาบาลสนามและโรงกรองน้ำเปิด (บัฟ + คะแนน) เหมืองหินให้คะแนนส่วนตัวเพิ่ม
Phase II|Fase II|Phase II|ช่วงที่ II
Canyon Captain spawns. Alliance with the most damage "defeats" it and gets the buffs.|Aparece el Capitán del Cañón. La alianza que más daño hace lo "derrota" y obtiene las bonificaciones.|Le Capitaine du Canyon apparaît. L'alliance qui inflige le plus de dégâts le « bat » et obtient les bonus.|กัปตันแคนยอนปรากฏ พันธมิตรที่ทำดาเมจมากที่สุด "ชนะ" และได้บัฟ
Phase III|Fase III|Phase III|ช่วงที่ III
Military Base opens – big points and combat boosts.|Se abre la Base militar: muchos puntos y mejoras de combate.|La Base militaire ouvre – beaucoup de points et des bonus de combat.|ฐานทัพทหารเปิด – คะแนนสูงและบูสต์การต่อสู้
Phase IV|Fase IV|Phase IV|ช่วงที่ IV
Energy Station produces Energy Cells (first after {0} min); carrying one to your Alliance Beacon gives huge points.|La Estación de energía produce Células de energía (la primera tras {0} min); llevar una a tu Baliza de alianza da muchísimos puntos.|La Station d'énergie produit des Cellules d'énergie (la première après {0} min) ; en apporter une à votre Balise d'alliance rapporte énormément de points.|สถานีพลังงานผลิตเซลล์พลังงาน (อันแรกหลัง {0} นาที) การนำไปที่บีคอนพันธมิตรให้คะแนนมหาศาล
Win condition|Condición de victoria|Condition de victoire|เงื่อนไขการชนะ
Higher Alliance (battlefield) points when time ends.|Más puntos de alianza (campo de batalla) al acabar el tiempo.|Plus de points d'alliance (champ de bataille) à la fin du temps.|มีคะแนนพันธมิตร (สนามรบ) สูงกว่าเมื่อหมดเวลา
Safety|Seguridad|Sécurité|ความปลอดภัย
Units do not die; injuries heal free after the battle. A free teleport is available every {0} minutes.|Las unidades no mueren; los heridos se curan gratis tras la batalla. Hay un teletransporte gratis cada {0} minutos.|Les unités ne meurent pas ; les blessés sont soignés gratuitement après la bataille. Une téléportation gratuite est disponible toutes les {0} minutes.|หน่วยไม่ตาย บาดเจ็บรักษาฟรีหลังการต่อสู้ มีเทเลพอร์ตฟรีทุก {0} นาที
Building points|Puntos por edificio|Points des bâtiments|คะแนนอาคาร
Objective|Objetivo|Objectif|เป้าหมาย
Alliance pts (capture / per min)|Pts de alianza (captura / por min)|Pts d'alliance (capture / par min)|คะแนนพันธมิตร (ยึด / ต่อนาที)
Personal pts (capture / per min)|Pts personales (captura / por min)|Pts personnels (capture / par min)|คะแนนส่วนตัว (ยึด / ต่อนาที)
Buff|Bonificación|Bonus|บัฟ
Energy Cell → Beacon|Célula de energía → Baliza|Cellule d'énergie → Balise|เซลล์พลังงาน → บีคอน
{0} per cell|{0} por célula|{0} par cellule|{0} ต่อเซลล์
Military Base|Base militar|Base militaire|ฐานทัพทหาร
{0} battlefield damage dealt, {1} damage taken|{0} daño infligido en el campo de batalla, {1} daño recibido|{0} dégâts infligés sur le champ de bataille, {1} dégâts subis|ดาเมจที่ทำในสนามรบ {0}, ดาเมจที่ได้รับ {1}
Field Hospital|Hospital de campaña|Hôpital de campagne|โรงพยาบาลสนาม
{0} battlefield healing speed, {1} healing cost|{0} velocidad de curación en el campo de batalla, {1} coste de curación|{0} vitesse de soin sur le champ de bataille, {1} coût des soins|ความเร็วรักษาในสนามรบ {0}, ค่ารักษา {1}
Water Refinery|Refinería de agua|Raffinerie d'eau|โรงกรองน้ำ
Quarry (gathering)|Cantera (recolección)|Carrière (récolte)|เหมืองหิน (เก็บทรัพยากร)
{0} per min|{0} por min|{0} par min|{0} ต่อนาที
{0}-minute cooldown after ore runs out|{0} minutos de espera cuando se agota el mineral|{0} minutes de recharge quand le minerai est épuisé|คูลดาวน์ {0} นาทีหลังแร่หมด
Defeating enemy units|Derrotar unidades enemigas|Vaincre des unités ennemies|กำจัดหน่วยศัตรู
{0} per {1} power defeated|{0} por cada {1} de poder derrotado|{0} pour {1} de puissance vaincue|{0} ต่อพลังที่กำจัด {1}
Canyon Captain|Capitán del Cañón|Capitaine du Canyon|กัปตันแคนยอน
{0} per {1} damage dealt|{0} por cada {1} de daño infligido|{0} par {1} de dégâts infligés|{0} ต่อดาเมจ {1}
Winner: {0} capture time, {1} alliance point yield, {2} damage dealt|Ganador: {0} tiempo de captura, {1} puntos de alianza obtenidos, {2} daño infligido|Vainqueur : {0} temps de capture, {1} gain de points d'alliance, {2} dégâts infligés|ผู้ชนะ: เวลายึด {0}, คะแนนพันธมิตรที่ได้ {1}, ดาเมจที่ทำ {2}
Rewards|Recompensas|Récompenses|รางวัล
Alliance (everyone)|Alianza (todos)|Alliance (tout le monde)|พันธมิตร (ทุกคน)
Team {0} win: chest, {1} weapon manuals, {2}× {3} diamonds, {4}× 1h build speed-ups (+more). Loss: smaller chest, {5} manuals, {6}× diamonds, {7}× speed-ups.|Victoria del Equipo {0}: cofre, {1} manuales de armas, {2}× {3} diamantes, {4}× aceleradores de construcción de 1 h (+más). Derrota: cofre más pequeño, {5} manuales, {6}× diamantes, {7}× aceleradores.|Victoire de l'Équipe {0} : coffre, {1} manuels d'armes, {2}× {3} diamants, {4}× accélérations de construction de 1 h (+ autres). Défaite : coffre plus petit, {5} manuels, {6}× diamants, {7}× accélérations.|ทีม {0} ชนะ: หีบ, คู่มืออาวุธ {1}, เพชร {2}× {3}, ตัวเร่งการสร้าง 1 ชม. {4}× (และอื่นๆ) แพ้: หีบเล็กกว่า, คู่มือ {5}, เพชร {6}×, ตัวเร่ง {7}×
Personal (entered battlefield)|Personal (entró al campo de batalla)|Personnel (entré sur le champ de bataille)|ส่วนตัว (เข้าสนามรบ)
Win: Lv4 chest, {0} manuals, {1}× diamonds, {2}× speed-ups. Loss: Lv3 chest, {3} manuals, {4}× diamonds, {5}× speed-ups.|Victoria: cofre Nv4, {0} manuales, {1}× diamantes, {2}× aceleradores. Derrota: cofre Nv3, {3} manuales, {4}× diamantes, {5}× aceleradores.|Victoire : coffre Nv4, {0} manuels, {1}× diamants, {2}× accélérations. Défaite : coffre Nv3, {3} manuels, {4}× diamants, {5}× accélérations.|ชนะ: หีบ Lv4, คู่มือ {0}, เพชร {1}×, ตัวเร่ง {2}× แพ้: หีบ Lv3, คู่มือ {3}, เพชร {4}×, ตัวเร่ง {5}×
Points tiers (winners who fought)|Niveles de puntos (ganadores que lucharon)|Paliers de points (vainqueurs ayant combattu)|ระดับคะแนน (ผู้ชนะที่ได้สู้)
{0}–{1}: {2} medals + {3} manuals + {4} troop & {5} healing speed-ups. {6}–{7}: {8} medals + {9} manuals + {10} + {11}. Higher tiers exist.|{0}–{1}: {2} medallas + {3} manuales + {4} aceleradores de tropas y {5} de curación. {6}–{7}: {8} medallas + {9} manuales + {10} + {11}. Hay niveles superiores.|{0}–{1} : {2} médailles + {3} manuels + {4} accélérations de troupes et {5} de soins. {6}–{7} : {8} médailles + {9} manuels + {10} + {11}. Il existe des paliers supérieurs.|{0}–{1}: เหรียญ {2} + คู่มือ {3} + ตัวเร่งทหาร {4} และตัวเร่งรักษา {5} / {6}–{7}: เหรียญ {8} + คู่มือ {9} + {10} + {11} มีระดับที่สูงกว่านี้
Lineup notes|Notas de alineación|Notes de composition|หมายเหตุการจัดทีม
Starters matter most|Los titulares son lo más importante|Les titulaires comptent le plus|ตัวจริงสำคัญที่สุด
Substitutes only get in if starters are missing when combat starts, so members who will actually show up belong in starter slots.|Los suplentes solo entran si faltan titulares al empezar el combate, así que los miembros que de verdad vayan a aparecer deben ocupar los puestos de titular.|Les remplaçants n'entrent que si des titulaires manquent au début du combat ; les membres qui seront vraiment là doivent donc être titulaires.|ตัวสำรองจะได้ลงเมื่อตัวจริงไม่มาตอนเริ่มต่อสู้เท่านั้น ดังนั้นสมาชิกที่จะมาจริงควรอยู่ในตำแหน่งตัวจริง
Team {0} unlock|Desbloqueo del Equipo {0}|Déblocage de l'Équipe {0}|ปลดล็อกทีม {0}
Needs at least {0} members scoring {1}+ in one battle the week before (roughly {2}–{3} minutes on a Quarry earns {4}).|Requiere al menos {0} miembros con {1}+ en una batalla la semana anterior (unos {2}–{3} minutos en una Cantera dan {4}).|Nécessite au moins {0} membres ayant marqué {1}+ en une bataille la semaine précédente (environ {2}–{3} minutes sur une Carrière rapportent {4}).|ต้องมีสมาชิกอย่างน้อย {0} คนที่ทำได้ {1}+ ในการต่อสู้ครั้งเดียวเมื่อสัปดาห์ก่อน (อยู่ที่เหมืองหินประมาณ {2}–{3} นาทีได้ {4})
Poll = availability|Encuesta = disponibilidad|Sondage = disponibilité|โพล = การว่าง
Each member's session vote also shows on the in-game Participants list; members who voted for the other session are likely unavailable.|El voto de sesión de cada miembro también aparece en la lista de Participantes del juego; quienes votaron por la otra sesión probablemente no estén disponibles.|Le vote de session de chaque membre apparaît aussi dans la liste des Participants du jeu ; ceux qui ont voté pour l'autre session sont probablement indisponibles.|โหวตรอบของสมาชิกแต่ละคนจะแสดงในรายชื่อผู้เข้าร่วมในเกมด้วย สมาชิกที่โหวตอีกรอบน่าจะไม่ว่าง
The Participants screen can switch from Personal Power to Arena Power (Total Power dropdown). Enter it on Canyon Teams if you want starters picked by it.|La pantalla de Participantes puede cambiar de Poder personal a Poder de arena (desplegable Poder total). Introdúcelo en Canyon Teams si quieres elegir titulares por él.|L'écran des Participants peut passer de la Puissance personnelle à la Puissance d'arène (menu Puissance totale). Saisissez-la dans Canyon Teams si vous voulez choisir les titulaires avec.|หน้าผู้เข้าร่วมสลับจากพลังส่วนตัวเป็นพลังอารีน่าได้ (เมนูพลังรวม) ใส่ค่านี้ใน Canyon Teams ถ้าต้องการเลือกตัวจริงตามค่านี้
#{0} by Arena|#{0} por arena|#{0} en arène|อันดับ {0} ตามอารีน่า
Close|Cerrar|Fermer|ปิด
H+V across {0} snapshots|H+V en {0} capturas|H+V sur {0} relevés|H+V ใน {0} ช่วงข้อมูล
Mod vehicle|Vehículo mod.|Véhicule mod.|ยานพาหนะม็อด
Canyon vote|Voto del Cañón|Vote Canyon|โหวตแคนยอน
Canyon slot|Puesto en el Cañón|Place au Canyon|ตำแหน่งแคนยอน
Game UID|UID del juego|UID du jeu|UID ในเกม
Auto ({0})|Auto ({0})|Auto ({0})|อัตโนมัติ ({0})
Auto (T1 Starter)|Auto (Titular E1)|Auto (Titulaire É1)|อัตโนมัติ (ตัวจริง T1)
Auto (T2 Starter)|Auto (Titular E2)|Auto (Titulaire É2)|อัตโนมัติ (ตัวจริง T2)
Auto (T1 Sub)|Auto (Suplente E1)|Auto (Remplaçant É1)|อัตโนมัติ (ตัวสำรอง T1)
Auto (T2 Sub)|Auto (Suplente E2)|Auto (Remplaçant É2)|อัตโนมัติ (ตัวสำรอง T2)
Auto (Bench)|Auto (Banquillo)|Auto (Banc)|อัตโนมัติ (ม้านั่งสำรอง)
Auto (Not available)|Auto (No disponible)|Auto (Indisponible)|อัตโนมัติ (ไม่ว่าง)
Auto (not placed)|Auto (sin asignar)|Auto (non placé)|อัตโนมัติ (ยังไม่จัด)
Passcode|Código|Code d'accès|รหัสผ่าน
Your name|Tu nombre|Votre nom|ชื่อของคุณ
Enter the alliance passcode to set availability; officers use the officer code to change slots. Changes reach the sheet within a minute.|Introduce el código de la alianza para fijar la disponibilidad; los oficiales usan el código de oficial para cambiar puestos. Los cambios llegan a la hoja en menos de un minuto.|Saisissez le code de l'alliance pour régler la disponibilité ; les officiers utilisent le code d'officier pour changer les places. Les changements arrivent dans la feuille en moins d'une minute.|ใส่รหัสพันธมิตรเพื่อตั้งค่าการว่าง เจ้าหน้าที่ใช้รหัสเจ้าหน้าที่เพื่อเปลี่ยนตำแหน่ง การเปลี่ยนแปลงจะไปถึงชีตภายในหนึ่งนาที
Member code accepted: you can set availability. Slots need the officer code.|Código de miembro aceptado: puedes fijar la disponibilidad. Los puestos requieren el código de oficial.|Code de membre accepté : vous pouvez régler la disponibilité. Les places nécessitent le code d'officier.|รับรหัสสมาชิกแล้ว: ตั้งค่าการว่างได้ ตำแหน่งต้องใช้รหัสเจ้าหน้าที่
Officer code accepted: you can change availability and slots.|Código de oficial aceptado: puedes cambiar disponibilidad y puestos.|Code d'officier accepté : vous pouvez changer la disponibilité et les places.|รับรหัสเจ้าหน้าที่แล้ว: เปลี่ยนการว่างและตำแหน่งได้
Change sent. The sheet picks it up within a minute and the board follows.|Cambio enviado. La hoja lo recoge en menos de un minuto y el panel se actualiza después.|Changement envoyé. La feuille le prend en compte en moins d'une minute et le tableau suit.|ส่งการเปลี่ยนแปลงแล้ว ชีตจะรับภายในหนึ่งนาทีและบอร์ดจะอัปเดตตาม
Changes go to the Canyon Teams sheet within a minute. Teams re-split right away as a preview.|Los cambios llegan a la hoja Canyon Teams en menos de un minuto. Los equipos se reparten de nuevo al momento como vista previa.|Les changements arrivent dans la feuille Canyon Teams en moins d'une minute. Les équipes sont recomposées tout de suite en aperçu.|การเปลี่ยนแปลงจะไปถึงชีต Canyon Teams ภายในหนึ่งนาที ทีมจะถูกแบ่งใหม่ทันทีเป็นตัวอย่าง
Availability and slot edits made here go to the Canyon Teams sheet through your Google Drive connection.|Los cambios de disponibilidad y puestos hechos aquí van a la hoja Canyon Teams a través de tu conexión con Google Drive.|Les modifications de disponibilité et de places faites ici vont dans la feuille Canyon Teams via votre connexion Google Drive.|การแก้ไขการว่างและตำแหน่งที่นี่จะไปที่ชีต Canyon Teams ผ่านการเชื่อมต่อ Google Drive ของคุณ
Google Drive is not connected in this view, so changes stay here as a preview. Connect Google Drive on claude.ai and reopen to sync with the sheet.|Google Drive no está conectado en esta vista, así que los cambios se quedan aquí como vista previa. Conecta Google Drive en claude.ai y vuelve a abrir para sincronizar con la hoja.|Google Drive n'est pas connecté dans cette vue, les changements restent donc ici en aperçu. Connectez Google Drive sur claude.ai et rouvrez pour synchroniser avec la feuille.|มุมมองนี้ไม่ได้เชื่อมต่อ Google Drive การเปลี่ยนแปลงจึงอยู่ที่นี่เป็นตัวอย่าง เชื่อมต่อ Google Drive บน claude.ai แล้วเปิดใหม่เพื่อซิงก์กับชีต
Copy UID|Copiar UID|Copier l'UID|คัดลอก UID
Copy summary|Copiar resumen|Copier le résumé|คัดลอกสรุป
Canyon date|Fecha del Cañón|Date du Canyon|วันที่แคนยอน
Roster = today's lineup ({0} players). Opponent, scores and points are optional.|Plantilla = alineación de hoy ({0} jugadores). Rival, marcadores y puntos son opcionales.|Effectif = composition du jour ({0} joueurs). Adversaire, scores et points sont facultatifs.|รายชื่อ = ทีมวันนี้ (ผู้เล่น {0} คน) คู่แข่ง คะแนนทีม และคะแนนผู้เล่นใส่หรือไม่ก็ได้
{0} subs played|{0} suplentes jugaron|{0} remplaçants ont joué|ตัวสำรองได้เล่น {0} คน
Opponent server|Servidor rival|Serveur adverse|เซิร์ฟเวอร์คู่แข่ง
Opponent alliance|Alianza rival|Alliance adverse|พันธมิตรคู่แข่ง
Opponent total power|Poder total del rival|Puissance totale adverse|พลังรวมของคู่แข่ง
Our score|Nuestro marcador|Notre score|คะแนนของเรา
Their score|Su marcador|Leur score|คะแนนคู่แข่ง
Result|Resultado|Résultat|ผล
Win|Victoria|Victoire|ชนะ
Loss|Derrota|Défaite|แพ้
No result yet|Sin resultado aún|Pas encore de résultat|ยังไม่มีผล
click a chip to switch Show / No-show|clic en una etiqueta para cambiar Presente / Ausente|cliquer sur une pastille pour basculer Présent / Absent|คลิกป้ายเพื่อสลับ มา / ไม่มา
Show|Presente|Présent|มา
Subs|Suplentes|Remplaçants|ตัวสำรอง
Not needed unless they played|No necesario salvo que jugaran|Pas nécessaire sauf s'ils ont joué|ไม่ได้ใช้ ยกเว้นได้ลงเล่น
Officer passcode|Código de oficial|Code d'officier|รหัสเจ้าหน้าที่
officer code|código de oficial|code d'officier|รหัสเจ้าหน้าที่
member or officer code|código de miembro u oficial|code de membre ou d'officier|รหัสสมาชิกหรือเจ้าหน้าที่
who is changing this|quién hace el cambio|qui fait ce changement|ใครเป็นคนเปลี่ยน
who is locking|quién registra|qui valide|ใครเป็นคนบันทึก
who is clearing|quién borra|qui efface|ใครเป็นคนล้าง
Lock in {0} players|Registrar {0} jugadores|Valider {0} joueurs|บันทึกผู้เล่น {0} คน
Save changes|Guardar cambios|Enregistrer les modifications|บันทึกการเปลี่ยนแปลง
Delete this Friday|Eliminar este viernes|Supprimer ce vendredi|ลบวันศุกร์นี้
Locking writes this Friday to the ledger (Trends → Canyon) and the tracker's Canyon Ledger tabs. Locking the same date again replaces it, so mistakes can be fixed. Your chips are kept on this device until you lock.|Registrar guarda este viernes en el historial (Tendencias → Cañón) y en las pestañas Canyon Ledger del tracker. Registrar la misma fecha otra vez la reemplaza, así que los errores se pueden corregir. Tus etiquetas se guardan en este dispositivo hasta que registres.|La validation enregistre ce vendredi dans le registre (Tendances → Canyon) et dans les onglets Canyon Ledger du tracker. Valider à nouveau la même date la remplace, les erreurs peuvent donc être corrigées. Vos pastilles restent sur cet appareil jusqu'à la validation.|การบันทึกจะเขียนวันศุกร์นี้ลงสมุดบันทึก (แนวโน้ม → แคนยอน) และแท็บ Canyon Ledger ของ tracker บันทึกวันเดิมซ้ำจะแทนที่ของเดิม จึงแก้ไขข้อผิดพลาดได้ ป้ายที่ตั้งไว้จะเก็บในอุปกรณ์นี้จนกว่าจะบันทึก
Also put {0} manual slots back on auto|También devolver {0} puestos manuales a automático|Remettre aussi {0} places manuelles en automatique|ตั้ง {0} ตำแหน่งที่กำหนดเองกลับเป็นอัตโนมัติด้วย
Clear {0} votes|Borrar {0} votos|Effacer {0} votes|ล้าง {0} โหวต
Cancel|Cancelar|Annuler|ยกเลิก
Everyone goes back to|Todos vuelven a|Tout le monde revient à|ทุกคนจะกลับไปเป็น
so this week's poll starts clean. Votes members send after this land on top of the reset; changes still waiting from before are dropped. T10 picks are kept (the sheet's Reset selections box clears those too). This cannot be undone from the board.|para que la encuesta de esta semana empiece de cero. Los votos que envíen los miembros después se aplican sobre el reinicio; los cambios pendientes de antes se descartan. Las selecciones T10 se mantienen (la casilla Reset selections de la hoja también las borra). Esto no se puede deshacer desde el panel.|pour que le sondage de cette semaine reparte de zéro. Les votes envoyés ensuite s'ajoutent après la remise à zéro ; les changements encore en attente sont abandonnés. Les choix T10 sont conservés (la case Reset selections de la feuille les efface aussi). Cette action ne peut pas être annulée depuis le tableau.|เพื่อให้โพลสัปดาห์นี้เริ่มใหม่ โหวตที่สมาชิกส่งหลังจากนี้จะมีผลหลังการรีเซ็ต การเปลี่ยนแปลงที่ค้างอยู่ก่อนหน้าจะถูกยกเลิก ตัวเลือก T10 ยังอยู่ (ช่อง Reset selections ในชีตจะล้างส่วนนั้นด้วย) ทำแล้วย้อนกลับจากบอร์ดไม่ได้
Find a member|Buscar un miembro|Trouver un membre|ค้นหาสมาชิก
Where the numbers come from|De dónde salen los números|D'où viennent les chiffres|ตัวเลขมาจากไหน
Switch between compact and full numbers|Cambiar entre números abreviados y completos|Basculer entre chiffres abrégés et complets|สลับตัวเลขแบบย่อและแบบเต็ม
Light / dark|Claro / oscuro|Clair / sombre|สว่าง / มืด
Language|Idioma|Langue|ภาษา
Arena: {0}|Arena: {0}|Arène : {0}|อารีน่า: {0}
Troops: {0}|Tropas: {0}|Troupes : {0}|กองทหาร: {0}
Structure: {0}|Estructuras: {0}|Bâtiments : {0}|สิ่งก่อสร้าง: {0}
Hero: {0}|Héroe: {0}|Héros : {0}|ฮีโร่: {0}
Tech: {0}|Tecnología: {0}|Technologie : {0}|เทคโนโลยี: {0}
Vehicle: {0}|Vehículo: {0}|Véhicule : {0}|ยานพาหนะ: {0}
{0} of total|{0} del total|{0} du total|{0} ของทั้งหมด
Alliance power by component|Poder de la alianza por componente|Puissance de l'alliance par composante|พลังพันธมิตรแยกตามส่วนประกอบ
Alliance hero plus vehicle power by snapshot|Poder de héroe más vehículo de la alianza por captura|Puissance héros plus véhicule de l'alliance par relevé|พลังฮีโร่บวกยานพาหนะของพันธมิตรตามช่วงข้อมูล
Filter by rank|Filtrar por rango|Filtrer par rang|กรองตามยศ
{0} members ({1})|{0} miembros ({1})|{0} membres ({1})|{0} คน ({1})
click to edit|clic para editar|cliquer pour modifier|คลิกเพื่อแก้ไข
Top gainers|Mayores subidas|Plus fortes hausses|เพิ่มขึ้นมากที่สุด
Top decliners|Mayores bajadas|Plus fortes baisses|ลดลงมากที่สุด
Search name|Buscar nombre|Chercher un nom|ค้นหาชื่อ
Swipe or drag to see more|Desliza o arrastra para ver más|Glissez ou faites glisser pour voir la suite|ปัดหรือลากเพื่อดูเพิ่ม
Scroll left|Desplazar a la izquierda|Défiler vers la gauche|เลื่อนไปทางซ้าย
Scroll right|Desplazar a la derecha|Défiler vers la droite|เลื่อนไปทางขวา
Scroll the table|Desplazar la tabla|Faire défiler le tableau|เลื่อนตาราง
Sort|Ordenar|Trier|เรียง
tag or name|etiqueta o nombre|tag ou nom|แท็กหรือชื่อ
Click to switch|Clic para cambiar|Cliquer pour changer|คลิกเพื่อสลับ
Live|En vivo|En direct|สด
Preview only|Solo vista previa|Aperçu seulement|ตัวอย่างเท่านั้น
Drive not connected|Drive no conectado|Drive non connecté|ไม่ได้เชื่อมต่อ Drive
Drive: reconnect|Drive: reconectar|Drive : reconnecter|Drive: เชื่อมต่อใหม่
Sync error|Error de sincronización|Erreur de synchronisation|ซิงก์ผิดพลาด
Saved|Guardado|Enregistré|บันทึกแล้ว
Saved {0}|Guardado {0}|Enregistré {0}|บันทึก {0} แล้ว
Locked in {0}|Registrado {0}|Validé {0}|บันทึก {0} แล้ว
Deleted {0}|Eliminado {0}|Supprimé {0}|ลบ {0} แล้ว
Delete the {0} Canyon from the ledger?|¿Eliminar del historial el Cañón del {0}?|Supprimer du registre le Canyon du {0} ?|ลบแคนยอนวันที่ {0} ออกจากสมุดบันทึกหรือไม่?
Power like 7.2B, 7200M or 7,200,000,000|Poder como 7.2B, 7200M o 7,200,000,000|Puissance comme 7.2B, 7200M ou 7,200,000,000|พลังเช่น 7.2B, 7200M หรือ 7,200,000,000
Enter the officer passcode|Introduce el código de oficial|Saisissez le code d'officier|ใส่รหัสเจ้าหน้าที่
Enter a passcode first|Primero introduce un código|Saisissez d'abord un code|ใส่รหัสก่อน
That passcode is not recognised|Ese código no es válido|Ce code n'est pas reconnu|ไม่รู้จักรหัสนี้
Clearing votes needs the officer code|Para borrar votos hace falta el código de oficial|Effacer les votes nécessite le code d'officier|การล้างโหวตต้องใช้รหัสเจ้าหน้าที่
The ledger needs the officer code|El historial requiere el código de oficial|Le registre nécessite le code d'officier|สมุดบันทึกต้องใช้รหัสเจ้าหน้าที่
Slots need the officer code|Los puestos requieren el código de oficial|Les places nécessitent le code d'officier|ตำแหน่งต้องใช้รหัสเจ้าหน้าที่
Cleared {0} votes|Borrados {0} votos|{0} votes effacés|ล้าง {0} โหวตแล้ว
Cleared {0} vote|Borrado {0} voto|{0} vote effacé|ล้าง {0} โหวตแล้ว
Cleared {0} votes and {1} slots|Borrados {0} votos y {1} puestos|{0} votes et {1} places effacés|ล้าง {0} โหวตและ {1} ตำแหน่งแล้ว
Cleared {0} members|Borrados {0} miembros|{0} membres effacés|ล้าง {0} คนแล้ว
the sheet follows within a minute|la hoja se actualiza en menos de un minuto|la feuille suit en moins d'une minute|ชีตจะอัปเดตตามภายในหนึ่งนาที
Could not reach the board API|No se pudo conectar con la API del panel|Impossible de joindre l'API du tableau|เชื่อมต่อ API ของบอร์ดไม่ได้
Sent to the sheet|Enviado a la hoja|Envoyé à la feuille|ส่งไปที่ชีตแล้ว
Google Drive needs to be reconnected|Hay que volver a conectar Google Drive|Google Drive doit être reconnecté|ต้องเชื่อมต่อ Google Drive ใหม่
Google Drive is not connected|Google Drive no está conectado|Google Drive n'est pas connecté|ไม่ได้เชื่อมต่อ Google Drive
Select and copy manually|Selecciona y copia a mano|Sélectionnez et copiez manuellement|เลือกและคัดลอกเอง
Copied|Copiado|Copié|คัดลอกแล้ว
Roster copied|Plantilla copiada|Effectif copié|คัดลอกรายชื่อแล้ว
Names copied|Nombres copiados|Noms copiés|คัดลอกชื่อแล้ว
Lineup copied|Alineación copiada|Composition copiée|คัดลอกรายชื่อทีมแล้ว
Reminder copied|Recordatorio copiado|Rappel copié|คัดลอกข้อความเตือนแล้ว
Summary copied|Resumen copiado|Résumé copié|คัดลอกสรุปแล้ว
UID copied|UID copiado|UID copié|คัดลอก UID แล้ว
JTB ID copied|JTB ID copiado|JTB ID copié|คัดลอก JTB ID แล้ว
Δ Arena|Δ Arena|Δ Arène|Δ อารีน่า
win rate|de victorias|de victoires|อัตราชนะ
{0} Win {1}–?|{0} Victoria {1}–?|{0} Victoire {1}–?|{0} ชนะ {1}–?
{0} Loss {1}–?|{0} Derrota {1}–?|{0} Défaite {1}–?|{0} แพ้ {1}–?
Locked {0} by {*}|Registrado el {0} por {*}|Validé le {0} par {*}|บันทึกเมื่อ {0} โดย {*}
edited {0} by {*}|editado el {0} por {*}|modifié le {0} par {*}|แก้ไขเมื่อ {0} โดย {*}
{0} matches with both powers. Ours is the starters' arena power at lock; theirs is whatever total power was entered, so treat it as a rough guide.|{0} partidas con ambos poderes. El nuestro es el poder de arena de los titulares al registrar; el suyo es el poder total que se introdujo, así que tómalo como una guía aproximada.|{0} matchs avec les deux puissances. La nôtre est la puissance d'arène des titulaires à la validation ; la leur est la puissance totale saisie, à prendre comme une indication approximative.|{0} แมตช์ที่มีพลังทั้งสองฝ่าย ของเราคือพลังอารีน่าของตัวจริงตอนบันทึก ของคู่แข่งคือพลังรวมที่กรอกไว้ ใช้เป็นแนวทางคร่าวๆ
{0} matches with both powers. Ours is the starters' power at lock; theirs is whatever total power was entered, so treat it as a rough guide.|{0} partidas con ambos poderes. El nuestro es el poder de los titulares al registrar; el suyo es el poder total que se introdujo, así que tómalo como una guía aproximada.|{0} matchs avec les deux puissances. La nôtre est la puissance des titulaires à la validation ; la leur est la puissance totale saisie, à prendre comme une indication approximative.|{0} แมตช์ที่มีพลังทั้งสองฝ่าย ของเราคือพลังของตัวจริงตอนบันทึก ของคู่แข่งคือพลังรวมที่กรอกไว้ ใช้เป็นแนวทางคร่าวๆ
{0} matches with both powers. Ours is the starters' hero + vehicle at lock; theirs is whatever total power was entered, so treat it as a rough guide.|{0} partidas con ambos poderes. El nuestro es el héroe + vehículo de los titulares al registrar; el suyo es el poder total que se introdujo, así que tómalo como una guía aproximada.|{0} matchs avec les deux puissances. La nôtre est le héros + véhicule des titulaires à la validation ; la leur est la puissance totale saisie, à prendre comme une indication approximative.|{0} แมตช์ที่มีพลังทั้งสองฝ่าย ของเราคือฮีโร่ + ยานพาหนะของตัวจริงตอนบันทึก ของคู่แข่งคือพลังรวมที่กรอกไว้ ใช้เป็นแนวทางคร่าวๆ
{0} match with both powers. Ours is the starters' arena power at lock; theirs is whatever total power was entered, so treat it as a rough guide.|{0} partida con ambos poderes. El nuestro es el poder de arena de los titulares al registrar; el suyo es el poder total que se introdujo, así que tómalo como una guía aproximada.|{0} match avec les deux puissances. La nôtre est la puissance d'arène des titulaires à la validation ; la leur est la puissance totale saisie, à prendre comme une indication approximative.|{0} แมตช์ที่มีพลังทั้งสองฝ่าย ของเราคือพลังอารีน่าของตัวจริงตอนบันทึก ของคู่แข่งคือพลังรวมที่กรอกไว้ ใช้เป็นแนวทางคร่าวๆ
{0} on {1}. The line starts with the second Friday.|{0} el {1}. La línea empieza con el segundo viernes.|{0} le {1}. La courbe commence au deuxième vendredi.|{0} เมื่อ {1} เส้นกราฟเริ่มที่วันศุกร์ที่สอง
Players · {0}|Jugadores · {0}|Joueurs · {0}|ผู้เล่น · {0}
"""
GLOSS = r"""
Alliance|Alianza|Alliance|พันธมิตร
Hero|Héroe|Héros|ฮีโร่
Vehicle|Vehículo|Véhicule|ยานพาหนะ
Science|Ciencia|Science|วิทยาศาสตร์
Structure|Estructuras|Bâtiments|สิ่งก่อสร้าง
Arena|Arena|Arène|อารีน่า
Troops|Tropas|Troupes|กองทหาร
Kills|Bajas|Éliminations|การสังหาร
Total|Total|Total|รวม
hero|héroe|héros|ฮีโร่
vehicle|vehículo|véhicule|ยานพาหนะ
science|ciencia|science|วิทยาศาสตร์
structure|estructuras|bâtiments|สิ่งก่อสร้าง
arena|arena|arène|อารีน่า
troops|tropas|troupes|กองทหาร
kills|bajas|éliminations|การสังหาร
total|total|total|รวม
power|poder|puissance|พลัง
by snapshot|por captura|par relevé|ตามช่วงข้อมูล
over time|a lo largo del tiempo|dans le temps|ตามเวลา
points|puntos|points|คะแนน
plus|más|plus|บวก
"""
