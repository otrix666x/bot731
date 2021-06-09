import telebot
from telebot import types
import config






choose_county = types.InlineKeyboardMarkup()
ukr = types.InlineKeyboardButton("🇺🇦Украина", callback_data="ukr")
rus = types.InlineKeyboardButton("🇷🇺Россия", callback_data="rus")
choose_county.row(ukr, rus)

main = types.InlineKeyboardMarkup()
cataloge = types.InlineKeyboardButton("🚬Выбор города", callback_data="city_urk")
profile = types.InlineKeyboardButton("👤Профиль", callback_data="prof_ukr")
info = types.InlineKeyboardButton("📖 Отзывы | Гарантии", callback_data="inf")
app_bal = types.InlineKeyboardButton("💰Пополнить баланс", callback_data="app")
chat = types.InlineKeyboardButton("💬Чат для клиентов", callback_data="chat")
job = types.InlineKeyboardButton("💼Работа", callback_data="job")
operator = types.InlineKeyboardButton("👨‍💻Оператор", url=f"{config.operator}")


main.row(cataloge, profile)
main.row(info,app_bal)
main.row(chat,job)
main.row(operator)

main_ru = types.InlineKeyboardMarkup()
cataloge_ru = types.InlineKeyboardButton("🚬Выбор города", callback_data="city_ru")
profile = types.InlineKeyboardButton("👤Профиль", callback_data="prof_ru")
info = types.InlineKeyboardButton("📖 Отзывы | Гарантии", callback_data="inf")
app_bal = types.InlineKeyboardButton("💰Пополнить баланс", callback_data="app")
chat = types.InlineKeyboardButton("💬Чат для клиентов", callback_data="chat")
job = types.InlineKeyboardButton("💼Работа", callback_data="job")
operator = types.InlineKeyboardButton("👨‍💻Оператор", url=f"{config.operator}")

main_ru.row(cataloge_ru, profile)
main_ru.row(info, app_bal)
main_ru.row(chat, job)
main_ru.row(operator)


city_urk = types.InlineKeyboardMarkup()

kiev = types.InlineKeyboardButton("♦️Київ", callback_data="Київ")
dnep = types.InlineKeyboardButton("♦️Дніпро", callback_data="Дніпро")
har = types.InlineKeyboardButton("♦️Харків", callback_data="Харків")
odes = types.InlineKeyboardButton("♦️Одеса", callback_data="Одеса")
lviv = types.InlineKeyboardButton("♦️Львів", callback_data="Львів")
kir = types.InlineKeyboardButton("♦️Кропивницький", callback_data="Кропивницький")
nik = types.InlineKeyboardButton("♦️Миколаїв", callback_data="Миколаїв")
zap = types.InlineKeyboardButton("♦️Запоріжжя", callback_data="Запоріжжя")
back = types.InlineKeyboardButton("🔙Вернуться в меню", callback_data="back1")
city_urk.row(kiev, dnep)
city_urk.row(har, odes)
city_urk.row(lviv, kir)
city_urk.row(nik, zap)
city_urk.row(back)


kiev_rayon = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton("🔙Вернуться к выбору города", callback_data="back2")

k1 = types.InlineKeyboardButton("♦️Голосіївський", callback_data="Голосіївський")
k2 = types.InlineKeyboardButton("♦️Дарницкий", callback_data="Дарницкий")
k3 = types.InlineKeyboardButton("♦️Дніпровський", callback_data="Дніпровський")
k4 = types.InlineKeyboardButton("♦️Оболонський", callback_data="Оболонський")
k5 = types.InlineKeyboardButton("♦️Подольский", callback_data="Подольский")
k6 = types.InlineKeyboardButton("♦️Солом'янський", callback_data="Солом'янський")

kiev_rayon.row(k1)
kiev_rayon.row(k2)
kiev_rayon.row(k3)
kiev_rayon.row(k4)
kiev_rayon.row(k5)
kiev_rayon.row(k6)
kiev_rayon.row(back1)

depr_rayon = types.InlineKeyboardMarkup()

d1 = types.InlineKeyboardButton("♦️Шевченківський", callback_data="Шевченківський")
d2 = types.InlineKeyboardButton("♦️Індустріальний", callback_data="Індустріальний")
d3 = types.InlineKeyboardButton("♦️Центральний", callback_data="Центральний")
d4 = types.InlineKeyboardButton("♦️Самарський", callback_data="Самарський")

depr_rayon.row(d1)
depr_rayon.row(d2)
depr_rayon.row(d3)
depr_rayon.row(d4)
depr_rayon.row(back1)


har_rayon = types.InlineKeyboardMarkup()

h1 = types.InlineKeyboardButton("♦️Київський", callback_data="Київський")
h2 = types.InlineKeyboardButton("♦️Московський", callback_data="Московський")

har_rayon.row(h1)
har_rayon.row(h2)
har_rayon.row(d2)
har_rayon.row(d1)
har_rayon.row(back1)

odessa_rayon = types.InlineKeyboardMarkup()

o1 = types.InlineKeyboardButton("♦️Малиновський", callback_data="malin")
o2 = types.InlineKeyboardButton("♦️Приморський", callback_data="prum")
o3 = types.InlineKeyboardButton("♦️Суворовський", callback_data="suv")

odessa_rayon.row(o1)
odessa_rayon.row(o2)
odessa_rayon.row(o3)
odessa_rayon.row(h2)
odessa_rayon.row(back1)

lviv_rayon = types.InlineKeyboardMarkup()
l1 = types.InlineKeyboardButton("Галицький", callback_data="Галицький")
l2 = types.InlineKeyboardButton("Личаківський", callback_data="Личаківський")
l3 = types.InlineKeyboardButton("Сихівський", callback_data="Сихівський")

lviv_rayon.row(l1)
lviv_rayon.row(l2)
lviv_rayon.row(l3)
lviv_rayon.row(d1)
lviv_rayon.row(back1)

kir_rayon = types.InlineKeyboardMarkup()
kr1 = types.InlineKeyboardButton("♦️Ленінський", callback_data="Ленінський")
kr2 = types.InlineKeyboardButton("♦️Кіровський", callback_data="Кіровський")
kir_rayon.row(kr1)
kir_rayon.row(kr2)
kir_rayon.row(back1)

nik_rayon = types.InlineKeyboardMarkup()
nik_rayon.row(d3)
nik_rayon.row(kr1)
nik_rayon.row(back1)


zapor_rayon = types.InlineKeyboardMarkup()
z1 = types.InlineKeyboardButton("♦️Олександрівський", callback_data="Олександрівський")
z2 = types.InlineKeyboardButton("♦️Комунарський", callback_data="Комунарський")
z3 = types.InlineKeyboardButton("♦️Дніпровський", callback_data="Дніпровський")
zapor_rayon.row(z1)
zapor_rayon.row(z2)
zapor_rayon.row(z3)
zapor_rayon.row(d1)
zapor_rayon.row(back1)

tovar_list = types.InlineKeyboardMarkup()
tov1 = types.InlineKeyboardButton("♦️ Кристалы MDMA (1гр)-600грн", callback_data="Кристалы MDMA (1гр)_600")
tov2 = types.InlineKeyboardButton("💎 Амф 💎 1(г)-450грн", callback_data="💎 Амф 💎 1(г)_450")
tov3 = types.InlineKeyboardButton("☮️ Шишки белая вдова ☮️ 1(г)-280гpн", callback_data="☮️ Шишки белая вдова ☮️ 1(г)_280")
tov4 = types.InlineKeyboardButton("☮️ Шишки белая вдова ☮️ 2(г)-450грн", callback_data="☮️ Шишки белая вдова ☮️ 2(г)_450")
tov5 = types.InlineKeyboardButton("☮️ Шишки чёрная вдова ☮️ 2(г)-470грн", callback_data="☮️ Шишки чёрная вдова ☮️ 2(г)_470")
tov6 = types.InlineKeyboardButton("⚡️ Альфа соль чёрная ⚡️ (1гр)-550гр", callback_data="⚡️ Альфа соль чёрная ⚡️ (1гр)_550")
tov7 = types.InlineKeyboardButton("🍯 Метадон 🍯 (1гр)-1200грн", callback_data="🍯 Метадон 🍯 (1гр)_1200")
tov8 = types.InlineKeyboardButton("☮️ Гаш ☮️ (1гр)-600грн", callback_data="☮️ Гаш ☮️ (1гр)_600")
tov9 = types.InlineKeyboardButton("⚡️ Альфа соль белая ⚡️ (1гр)-450грн", callback_data="⚡️ Альфа соль белая ⚡️ (1гр)_450")
tov10 = types.InlineKeyboardButton("🍚 Меф кристаллы 🍚 (1гр)-400грн", callback_data="🍚 Меф кристаллы 🍚 (1гр)_400")

tovar_list.row(tov1)
tovar_list.row(tov2)
tovar_list.row(tov3)
tovar_list.row(tov4)
tovar_list.row(tov5)
tovar_list.row(tov6)
tovar_list.row(tov7)
tovar_list.row(tov8)
tovar_list.row(tov9)
tovar_list.row(tov10)
tovar_list.row(back)
tovar_list.row(back1)


ru_city = types.InlineKeyboardMarkup()
msc = types.InlineKeyboardButton("♦️Москва", callback_data="Москва")
spb = types.InlineKeyboardButton("♦️Санкт-Петербург", callback_data="Санкт-Петербург")
ekb = types.InlineKeyboardButton("♦️Екатеринбург", callback_data="Екатеринбург")
brnl = types.InlineKeyboardButton("♦️Барнаул", callback_data="Барнаул")
tomsk = types.InlineKeyboardButton("♦️Томск", callback_data="Томск")
tumen = types.InlineKeyboardButton("♦️Тюмень", callback_data="Тюмень")
nijniy = types.InlineKeyboardButton("♦️Нижний Новгород", callback_data="Нижний Новгород")
samara = types.InlineKeyboardButton("♦️Самара", callback_data="Самара")
omsk = types.InlineKeyboardButton("♦️Омск", callback_data="Омск")
sarat = types.InlineKeyboardButton("♦️Саратов", callback_data="Саратов")
krsndr = types.InlineKeyboardButton("♦️Краснодар", callback_data="Краснодар")
krsn = types.InlineKeyboardButton("♦️Красноярск", callback_data="Красноярск")
voron = types.InlineKeyboardButton("♦️Воронеж", callback_data="Воронеж")
volg = types.InlineKeyboardButton("♦️Волгоград", callback_data="Волгоград")
ufa = types.InlineKeyboardButton("♦️Уфа", callback_data="Уфа")
rostov = types.InlineKeyboardButton("♦️Ростов-на-Дону", callback_data="Ростов-на-Дону")
irk = types.InlineKeyboardButton("♦️Иркутск", callback_data="Иркутск")
mah = types.InlineKeyboardButton("♦️Махачкала", callback_data="Махачкала")
back2 = types.InlineKeyboardButton("🔙Вернуться в меню", callback_data="back3")
back3 = types.InlineKeyboardButton("🔙Вернуться к выбору города", callback_data="back4")
ru_city.row(msc, spb)
ru_city.row(ekb, brnl)
ru_city.row(tomsk, tumen)
ru_city.row(nijniy, samara)
ru_city.row(omsk, sarat)
ru_city.row(krsndr, krsn)
ru_city.row(voron, volg)
ru_city.row(ufa, rostov)
ru_city.row(irk,mah)
ru_city.row(back2)


msc_rayon = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton("♦️САО", callback_data="САО")
m2 = types.InlineKeyboardButton("♦️ЦАО", callback_data="ЦАО")
m3 = types.InlineKeyboardButton("♦️ЮАО", callback_data="ЮАО")
m4 = types.InlineKeyboardButton("♦️ЮВАО", callback_data="ЮВАО")
m5 = types.InlineKeyboardButton("♦️ЗАО", callback_data="ЗАО")
msc_rayon.row(m1)
msc_rayon.row(m2)
msc_rayon.row(m3)
msc_rayon.row(m4)
msc_rayon.row(m5)
msc_rayon.row(back3)

spb_rayon = types.InlineKeyboardMarkup()
sp1 = types.InlineKeyboardButton("Василеостровский", callback_data="Василеостровский")
sp2 = types.InlineKeyboardButton("Выборгский", callback_data="Выборгский")
sp3 = types.InlineKeyboardButton("Калининский", callback_data="Калининский")
sp4 = types.InlineKeyboardButton("Кировский", callback_data="Кировский")
sp5 = types.InlineKeyboardButton("Курортный", callback_data="Курортный")
sp6 = types.InlineKeyboardButton("Московский", callback_data="Московский")
sp7 = types.InlineKeyboardButton("Приморский", callback_data="Приморский")
sp8 = types.InlineKeyboardButton("Фрунзенский", callback_data="Фрунзенский")
sp9 = types.InlineKeyboardButton("Центральный", callback_data="Центральный")
spb_rayon.row(sp1)
spb_rayon.row(sp2)
spb_rayon.row(sp3)
spb_rayon.row(sp4)
spb_rayon.row(sp5)
spb_rayon.row(sp6)
spb_rayon.row(sp7)
spb_rayon.row(sp8)
spb_rayon.row(sp9)
spb_rayon.row(back3)

ekb_rayon = types.InlineKeyboardMarkup()
ek1  = types.InlineKeyboardButton("♦️Железнодорожный", callback_data="Железнодорожный")
ek2  = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
ek3  = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
ek4  = types.InlineKeyboardButton("♦️Ордожиникидзевский", callback_data="Ордожиникидзевский")
ek5  = types.InlineKeyboardButton("♦️Чкаловский", callback_data="Чкаловский")
ekb_rayon.row(ek1)
ekb_rayon.row(ek2)
ekb_rayon.row(ek3)
ekb_rayon.row(ek4)
ekb_rayon.row(ek5)
ekb_rayon.row(back3)

brnl_rayon = types.InlineKeyboardMarkup()
brn1 = types.InlineKeyboardButton("♦️Железнодорожный",callback_data="Железнодорожный")
brn2 = types.InlineKeyboardButton("♦️Индустриальный",callback_data="Индустриальный")
brn3 = types.InlineKeyboardButton("♦️Ленинский",callback_data="Ленинский")
brn4 = types.InlineKeyboardButton("♦️Октябрьский",callback_data="Октябрьский")
brn5 = types.InlineKeyboardButton("♦️Центральный",callback_data="Центральный")
brnl_rayon.row(brn1)
brnl_rayon.row(brn2)
brnl_rayon.row(brn3)
brnl_rayon.row(brn4)
brnl_rayon.row(brn5)
brnl_rayon.row(back3)

tomsk_rayon = types.InlineKeyboardMarkup()
tm1 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
tm2 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
tm3 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
tm4 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
tomsk_rayon.row(tm1)
tomsk_rayon.row(tm2)
tomsk_rayon.row(tm3)
tomsk_rayon.row(tm4)
tomsk_rayon.row(back3)

tumen_rayon = types.InlineKeyboardMarkup()
tum1 = types.InlineKeyboardButton("♦️Восточный", callback_data="Восточный")
tum2 = types.InlineKeyboardButton("♦️Калининский", callback_data="Калининский")
tum3 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
tum4 = types.InlineKeyboardButton("♦️Центральный", callback_data="Центральный")
tumen_rayon.row(tum1)
tumen_rayon.row(tum2)
tumen_rayon.row(tum3)
tumen_rayon.row(tum4)
tumen_rayon.row(back3)


nijniy_rayon = types.InlineKeyboardMarkup()
nij1 = types.InlineKeyboardButton("♦️Автозаводский", callback_data="Автозаводский")
nij2 = types.InlineKeyboardButton("♦️Канавинский", callback_data="Канавинский")
nij3 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
nij4 = types.InlineKeyboardButton("♦️Московский", callback_data="Московский")
nij5 = types.InlineKeyboardButton("♦️Нижегородский", callback_data="Нижегородский")
nij6 = types.InlineKeyboardButton("♦️Приокский", callback_data="Приокский")
nij7 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
nijniy_rayon.row(nij1)
nijniy_rayon.row(nij2)
nijniy_rayon.row(nij3)
nijniy_rayon.row(nij4)
nijniy_rayon.row(nij5)
nijniy_rayon.row(nij6)
nijniy_rayon.row(nij7)
nijniy_rayon.row(back3)


samara_rayon = types.InlineKeyboardMarkup()
sam1 = types.InlineKeyboardButton("♦️Самарский", callback_data="Самарский")
sam2 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
sam3 = types.InlineKeyboardButton("♦️Железнодорожный", callback_data="Железнодорожный")
sam4 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
sam5 = types.InlineKeyboardButton("♦️Промышленный", callback_data="Промышленный")
sam6 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
sam7 = types.InlineKeyboardButton("♦️Красноглинский", callback_data="Красноглинский")
samara_rayon.row(sam1)
samara_rayon.row(sam2)
samara_rayon.row(sam3)
samara_rayon.row(sam4)
samara_rayon.row(sam5)
samara_rayon.row(sam6)
samara_rayon.row(sam7)
samara_rayon.row(back3)


omsk_rayon = types.InlineKeyboardMarkup()
om1 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
om2 = types.InlineKeyboardButton("♦️Центральный", callback_data="Центральный")
om3 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
om4 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
omsk_rayon.row(om1)
omsk_rayon.row(om2)
omsk_rayon.row(om3)
omsk_rayon.row(om4)
omsk_rayon.row(back3)


sarat_rayon = types.InlineKeyboardMarkup()
sar1 = types.InlineKeyboardButton("♦️Заводской",callback_data="Заводской")
sar2 = types.InlineKeyboardButton("♦️Октрябрьский",callback_data="Октрябрьский")
sar3 = types.InlineKeyboardButton("♦️Фрунзенский",callback_data="Фрунзенский")
sar4 = types.InlineKeyboardButton("♦️Волжский",callback_data="Волжский")
sar5 = types.InlineKeyboardButton("♦️Ленинский",callback_data="Ленинский")
sar6 = types.InlineKeyboardButton("♦️Кировский",callback_data="Кировский")
sarat_rayon.row(sar1)
sarat_rayon.row(sar2)
sarat_rayon.row(sar3)
sarat_rayon.row(sar4)
sarat_rayon.row(sar5)
sarat_rayon.row(sar6)
sarat_rayon.row(back3)

krsndr_rayon = types.InlineKeyboardMarkup()
krsn1 = types.InlineKeyboardButton("♦️ЖМР", callback_data="ЖМР")
krsn2 = types.InlineKeyboardButton("♦️СМР", callback_data="СМР")
krsn3 = types.InlineKeyboardButton("♦️ЗИП", callback_data="ЗИП")
krsn4 = types.InlineKeyboardButton("♦️РИП", callback_data="РИП")
krsn5 = types.InlineKeyboardButton("♦️Центральный", callback_data="Центральный")
krsn6 = types.InlineKeyboardButton("♦️ШМР", callback_data="ШМР")
krsn7 = types.InlineKeyboardButton("♦️ЮМР", callback_data="ЮМР")
krsn8 = types.InlineKeyboardButton("♦️КМР", callback_data="КМР")
krsn9 = types.InlineKeyboardButton("♦️ПМР", callback_data="ПМР")
krsn10 = types.InlineKeyboardButton("♦️ГМР", callback_data="ГМР")
krsn11= types.InlineKeyboardButton("♦️ЧМР", callback_data="ЧМР")

krsndr_rayon.row(krsn1)
krsndr_rayon.row(krsn2)
krsndr_rayon.row(krsn3)
krsndr_rayon.row(krsn4)
krsndr_rayon.row(krsn5)
krsndr_rayon.row(krsn6)
krsndr_rayon.row(krsn7)
krsndr_rayon.row(krsn8)
krsndr_rayon.row(krsn9)
krsndr_rayon.row(krsn10)
krsndr_rayon.row(krsn11)
krsndr_rayon.row(back3)

krsn_rayon = types.InlineKeyboardMarkup()
krs1 = types.InlineKeyboardButton("♦️Железнодорожный",callback_data="Железнодорожный")
krs2 = types.InlineKeyboardButton("♦️Кировский",callback_data="Кировский")
krs3 = types.InlineKeyboardButton("♦️Ленинский",callback_data="Ленинский")
krs4 = types.InlineKeyboardButton("♦️Свердловский",callback_data="Свердловский")
krs5 = types.InlineKeyboardButton("♦️Советский",callback_data="Советский")
krs6 = types.InlineKeyboardButton("♦️Центральный",callback_data="Центральный")
krsn_rayon.row(krs1)
krsn_rayon.row(krs2)
krsn_rayon.row(krs3)
krsn_rayon.row(krs4)
krsn_rayon.row(krs5)
krsn_rayon.row(krs6)
krsn_rayon.row(back3)


voron_rayon = types.InlineKeyboardMarkup()
vor1 = types.InlineKeyboardButton("♦️Железнодорожный", callback_data="Железнодорожный")
vor2 = types.InlineKeyboardButton("♦️Коминтерновский", callback_data="Коминтерновский")
vor3 = types.InlineKeyboardButton("♦️Левобережный", callback_data="Левобережный")
vor4 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
vor5 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
vor6 = types.InlineKeyboardButton("♦️Центральный", callback_data="Центральный")
voron_rayon.row(vor1)
voron_rayon.row(vor2)
voron_rayon.row(vor3)
voron_rayon.row(vor4)
voron_rayon.row(vor5)
voron_rayon.row(vor6)
voron_rayon.row(back3)

volg_rayon = types.InlineKeyboardMarkup()
vol1 = types.InlineKeyboardButton("♦️Ворошиловский",callback_data="Ворошиловский")
vol2 = types.InlineKeyboardButton("♦️Дзержинский",callback_data="Дзержинский")
vol3 = types.InlineKeyboardButton("♦️Тракторозаводский",callback_data="Тракторозаводский")
vol4 = types.InlineKeyboardButton("♦️Кировский",callback_data="Кировский")
vol5 = types.InlineKeyboardButton("♦️Советский",callback_data="Советский")
vol6 = types.InlineKeyboardButton("♦️Центральный",callback_data="Центральный")
volg_rayon.row(vol1)
volg_rayon.row(vol2)
volg_rayon.row(vol3)
volg_rayon.row(vol4)
volg_rayon.row(vol5)
volg_rayon.row(vol6)
volg_rayon.row(back3)

ufa_rayon = types.InlineKeyboardMarkup()
uf1 = types.InlineKeyboardButton("♦️Демский", callback_data="Демский")
uf2 = types.InlineKeyboardButton("♦️Калининский", callback_data="Калининский")
uf3 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
uf4 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
uf5 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
uf6 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
ufa_rayon.row(uf1)
ufa_rayon.row(uf2)
ufa_rayon.row(uf3)
ufa_rayon.row(uf4)
ufa_rayon.row(uf5)
ufa_rayon.row(uf6)
ufa_rayon.row(back3)

rostov_rayon = types.InlineKeyboardMarkup()
ros1 = types.InlineKeyboardButton("♦️Ворошиловский", callback_data="Ворошиловский")
ros2 = types.InlineKeyboardButton("♦️Железнодорожный", callback_data="Железнодорожный")
ros3 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
ros4 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
ros5 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
ros6 = types.InlineKeyboardButton("♦️Первомайский", callback_data="Первомайский")
ros7 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
rostov_rayon.row(ros1)
rostov_rayon.row(ros2)
rostov_rayon.row(ros3)
rostov_rayon.row(ros4)
rostov_rayon.row(ros5)
rostov_rayon.row(ros6)
rostov_rayon.row(ros7)
rostov_rayon.row(back3)

irk_rayon = types.InlineKeyboardMarkup()
ir1 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
ir2 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
ir3 = types.InlineKeyboardButton("♦️Октябрьский", callback_data="Октябрьский")
ir4 = types.InlineKeyboardButton("♦️Свердловский", callback_data="Свердловский")
irk_rayon.row(ir1)
irk_rayon.row(ir2)
irk_rayon.row(ir3)
irk_rayon.row(ir4)
irk_rayon.row(back3)

mah_rayon = types.InlineKeyboardMarkup()
mh1 = types.InlineKeyboardButton("♦️Кировский", callback_data="Кировский")
mh2 = types.InlineKeyboardButton("♦️Советский", callback_data="Советский")
mh3 = types.InlineKeyboardButton("♦️Ленинский", callback_data="Ленинский")
mah_rayon.row(mh1)
mah_rayon.row(mh2)
mah_rayon.row(mh3)
mah_rayon.row(back3)


rutovar_list = types.InlineKeyboardMarkup()

rutov1 = types.InlineKeyboardButton("💎 Скорость a-PVP 💎 0.5(г)-1400р", callback_data="💎 Скорость a-PVP 💎 0.5(г)_1400")
rutov2 = types.InlineKeyboardButton("💎 Скорость a-PVP 💎 1(г)-2600р", callback_data="💎 Скорость a-PVP 💎 1(г)_2600")
rutov3 = types.InlineKeyboardButton("☮️ Гашиш [Афганский] ☮️ 1(г)-2300p", callback_data="☮️ Гашиш [Афганский] ☮️ 1(г)_2300")
rutov4 = types.InlineKeyboardButton("☮️ Гашиш VHQ Lemon | Ice-o-lator ☮️ 2(г)-4300р", callback_data="☮️ Гашиш VHQ Lemon ☮️ 2(г)_4300")
rutov5 = types.InlineKeyboardButton("☮️ Гашиш VHQ Black Mamba | Ice-o-lator ☮️ 2(г)-4300р", callback_data="☮️ Гашиш VHQ Black Mamba☮️ 2(г)_4300")
rutov6 = types.InlineKeyboardButton("☮️ Гашиш VHQ Paris | Ice-o-lator ☮️ (2г)-4300р", callback_data="☮️ Гашиш VHQ Paris☮️ (2г)_4300")
rutov7 = types.InlineKeyboardButton("☮️ White Widow ☮️ (1г)-1800р", callback_data="☮️ White Widow ☮️ (1г)_1800")
rutov8 = types.InlineKeyboardButton("☮️ Бошки убойные LSD ☮️ (2г)-3200р", callback_data="☮️ Бошки убойные LSD ☮️ (2г)_3200")
rutov9 = types.InlineKeyboardButton("☮️ AK-47 ☮️ (1г)-1750р", callback_data="☮️ AK-47 ☮️ (1г)_1750")
rutov10 = types.InlineKeyboardButton("⚡️ [HYDRA TEST 96.89%] Амфетамин White Power ⚡️ (1г)-1300р", callback_data="⚡️Амфетамин White Power ⚡️ (1г)_1300")
rutov11 = types.InlineKeyboardButton("⚡️ Амфетамин White Luxury ⚡️ (1г)-1400р", callback_data="⚡️ Амфетамин White Luxury ⚡️ (1г)_1400")
rutov12 = types.InlineKeyboardButton("⚡️ Амфетамин White Luxury ⚡️ (2г)-2500р", callback_data="⚡️ Амфетамин White Luxury ⚡️ (2г)_2500")
rutov13 = types.InlineKeyboardButton("❤️ Мефедрон [Мука] ❤️ (1г)-1600р", callback_data="❤️ Мефедрон [Мука] ❤️ (1г)_1600")
rutov14 = types.InlineKeyboardButton("❤️ [LUX!!!] Мефедрон [Crystal Meal] ❤️ (1г)-1990р", callback_data="❤️ [LUX!!!] Мефедрон ❤️ (1г)_1990")
rutov15 = types.InlineKeyboardButton("♦️ МДМА (1гр)-2800p", callback_data="♦️ МДМА (1гр)_2800")
rutov16 = types.InlineKeyboardButton("♦️ МДМА (2гр)-5600p", callback_data="♦️ МДМА (2гр)_5600")
rutov17 = types.InlineKeyboardButton("🍯 Метадон 🍯 (0.5г)-3700р", callback_data="🍯 Метадон 🍯 (0.5г)_3700")
rutov18 = types.InlineKeyboardButton("🍯 Метадон 🍯 (1г)-5800р", callback_data="🍯 Метадон 🍯 (1г)_5800")
rutov19 = types.InlineKeyboardButton("🍚 Героин 🍚 (1г)-3500р", callback_data="🍚 Героин 🍚 (1г)_3500")
rutov20 = types.InlineKeyboardButton("⚡️ LUXURY COCAINE [AUDI] ⚡️ (0.5г)-4500p", callback_data="⚡️ LUXURY COCAINE [AUDI] ⚡️ (0.5г)_4500")
rutov21 = types.InlineKeyboardButton("⚡️ LUXURY COCAINE [AUDI] ⚡️ (1г)-8500p", callback_data="⚡️ LUXURY COCAINE [AUDI] ⚡️ (1г)_8500")
rutov22 = types.InlineKeyboardButton("★ Кокаин 24 Colombia ★ (0.5г)-6500p", callback_data="★ Кокаин 24 Colombia ★ (0.5г)_6500")
rutov23 = types.InlineKeyboardButton("★ VHQ Кокаин DTJ Colombia★ (0,5г)-6500p", callback_data="★ VHQ Кокаин DTJ Colombia★ (0,5г)_6500")
rutov24 = types.InlineKeyboardButton("🎇LSD: Марки 220 - 250 мкг🎇 (5шт)-3500p", callback_data="🎇LSD: Марки 220 - 250 мкг🎇 (5шт)_3500")
rutov25 = types.InlineKeyboardButton("❄️Метамфетамин HQ(Крис)❄️ (1г)-3400p", callback_data="❄️Метамфетамин HQ(Крис)❄️ (1г)_3400")

rutovar_list.row(rutov1)
rutovar_list.row(rutov2)
rutovar_list.row(rutov3)
rutovar_list.row(rutov4)
rutovar_list.row(rutov5)
rutovar_list.row(rutov6)
rutovar_list.row(rutov7)
rutovar_list.row(rutov8)
rutovar_list.row(rutov9)
rutovar_list.row(rutov10)
rutovar_list.row(rutov11)
rutovar_list.row(rutov12)
rutovar_list.row(rutov13)
rutovar_list.row(rutov14)
rutovar_list.row(rutov15)
rutovar_list.row(rutov16)
rutovar_list.row(rutov17)
rutovar_list.row(rutov18)
rutovar_list.row(rutov19)
rutovar_list.row(rutov20)
rutovar_list.row(rutov21)
rutovar_list.row(rutov22)
rutovar_list.row(rutov23)
rutovar_list.row(rutov24)
rutovar_list.row(rutov25)
rutovar_list.row(back3)


prof_ukrbut = types.InlineKeyboardMarkup()
but1 = types.InlineKeyboardButton("📥Пополнить баланс", callback_data="Пополнить баланс")

prof_ukrbut.row(but1, back)

prof_rubut = types.InlineKeyboardMarkup()
prof_rubut.row(but1, back2)

delete = types.InlineKeyboardMarkup()
delete.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))

nomoney = types.InlineKeyboardMarkup()
nomoney.row(but1,(types.InlineKeyboardButton("❌Закрыть", callback_data="delete")))



admin_but = types.ReplyKeyboardMarkup(True)
admin_but.add("🔈Сделать рассылку🔈", "💥кол-во пользователей💥")
admin_but.add("⚡️Сменить баланс⚡️")


add_balance = types.InlineKeyboardMarkup()
add_balance.row(types.InlineKeyboardButton("🥝QIWI", callback_data="qiwi"),(types.InlineKeyboardButton("💳Карта", callback_data="card")))
add_balance.row(types.InlineKeyboardButton("💲BTC", callback_data="btc"),(types.InlineKeyboardButton("❌Закрыть", callback_data="delete")))





































































