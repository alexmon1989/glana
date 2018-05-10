from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['products'] = [
            {
                'name': "Бейджи",
                'type': "polygraphy",
                'add_text': "пластиковые, металлические, бумажные",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Билеты и купоны",
                'type': "polygraphy",
                'add_text': "любые форматы: A6, A7, A8",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Блоки для записей",
                'type': "polygraphy",
                'add_text': "кубарики с вашим фирменным принтом",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Бирки, этикетки, лейблы",
                'type': "polygraphy",
                'add_text': "для одежды и не только",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Блокноты",
                'type': "polygraphy",
                'add_text': "любые форматы: A4, A5, A6. На пружине и без",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Брошюры",
                'type': "polygraphy",
                'add_text': "любые форматы: A4, A5, A6",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Буклеты",
                'type': "polygraphy",
                'add_text': "любые форматы: A4, A5, A6",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Визитки",
                'type': "polygraphy",
                'add_text': "стандартные, евро, эксключивные, на необычных материалах",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Визитки",
                'type': "polygraphy",
                'add_text': "стандартные, евровизитки, эксключивные, на необычных материалах",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Воблеры",
                'type': "polygraphy",
                'add_text': "бумажные и картонные рекламные воблеры",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Грамоты, дипломы",
                'type': "polygraphy",
                'add_text': "дипломы, сертификаты, почетные грамоты на любых материалах, в т.ч. на металле.",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Журналы",
                'type': "polygraphy",
                'add_text': "печать глянцевых журналов",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Календари",
                'type': "polygraphy",
                'add_text': "настольные, настенные, перекидные, календари-плакаты и т.д.",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Каталоги",
                'type': "polygraphy",
                'add_text': "мягкий переплёт, сшивка на пружину или скобу",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Книги",
                'type': "polygraphy",
                'add_text': "мягкий переплёт, твёрдый переплёт",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Конверты",
                'type': "polygraphy",
                'add_text': "печать фирменных логотипов на конвертах",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Листовки",
                'type': "polygraphy",
                'add_text': "рекламные листовки любых форматов: A6, A5, A4, A3",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Меню и сеты",
                'type': "polygraphy",
                'add_text': "меню и сеты разных форматов для ресторанного бизнеса",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Наклейки",
                'type': "polygraphy",
                'add_text': "наклейки A5, A6 и других форматов, наклейки на авто",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Открытки",
                'type': "polygraphy souvenir",
                'add_text': "почтовые и поздравительные открытки любых форматов",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Пакеты",
                'type': "polygraphy",
                'add_text': "печать на бумажных пакетах",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Упаковки",
                'type': "polygraphy",
                'add_text': "печать на подарочных, фирменных, упаковках для еды",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Плакаты",
                'type': "polygraphy",
                'add_text': "печать плакатов формата A3, A2, A1",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Сертификаты, пластиковые карты",
                'type': "polygraphy",
                'add_text': "печать сертификатов, подарочных карт",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Стикеры",
                'type': "polygraphy",
                'add_text': "печать на стикерах фирменных логотипов и пр.",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Таблички, вывески, указатели",
                'type': "polygraphy souvenir",
                'add_text': "изготовление пластиковых табличек, знаков и пр.",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Фирменные бланки",
                'type': "polygraphy",
                'add_text': "печать фирменных бланков любого формата",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Флаеры",
                'type': "polygraphy",
                'add_text': "еврофлаеры, премиум-флаеры, нестандартные флаеры",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Хенгеры",
                'type': "polygraphy",
                'add_text': "фигурные флаеры с крючком для крепления на дверные ручки",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Ценники",
                'type': "polygraphy",
                'add_text': "ценники на картоне или самоклеющиеся",
                'image': 'img/img-temp/400x270/img1.jpg'
            },

            {
                'name': "Коврики для мышки",
                'type': "souvenir",
                'add_text': "печать фирменных логотипов и не только на ковриках для мыши",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Пазлы",
                'type': "souvenir",
                'add_text': "печать пазлов формата A3, A4, A5 с вашим изображением",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Зажигалки",
                'type': "souvenir",
                'add_text': "печать фирменных логотипов и не только на зажигалках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Ручки",
                'type': "souvenir",
                'add_text': "печать фирменных логотипов и не только на ручках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Флешках",
                'type': "souvenir",
                'add_text': "печать фирменных логотипов и не только на флешках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Чашки",
                'type': "souvenir",
                'add_text': "печать фирменных логотипов и не только на чашках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },

            {
                'name': "Футболки",
                'type': "souvenir clothes",
                'add_text': "печать изображений, текста на футболках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Толстовки, регланы",
                'type': "souvenir clothes",
                'add_text': "печать изображений, текста на толстовках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Бейсболки",
                'type': "souvenir clothes",
                'add_text': "печать изображений, текста на бейсболках",
                'image': 'img/img-temp/400x270/img1.jpg'
            },

            {
                'name': "Интерьерная печать",
                'type': "large-format-printing",
                'add_text': "для размещения напечатанной продукции внутри помещений",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Печать на Oracal и пластике",
                'type': "large-format-printing",
                'add_text': "печать больших форматов на клеющейся плёнки и пластике",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Печать на холсте, бумаге",
                'type': "large-format-printing",
                'add_text': "печать больших форматов на бумажных носителях",
                'image': 'img/img-temp/400x270/img1.jpg'
            },

            {
                'name': "Биговка",
                'type': "services",
                'add_text': "нанесение линии сгиба на лист",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Дизайн рекламы",
                'type': "services",
                'add_text': "разработка дизайна любой сложности",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Изготовление штанц-форм",
                'type': "services",
                'add_text': "ротационные и плоские штанц-формы",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Лазерная гравировка",
                'type': "services",
                'add_text': "нанесение изображений с помощью лазерного луча",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Ламинирование",
                'type': "services",
                'add_text': "покрытие полиграфической продукции плёнкой",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Порезка",
                'type': "services",
                'add_text': "плоттерная порезка самоклеющейся бумаги для наклеек и стикеров",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Прикатка плёнки",
                'type': "services",
                'add_text': "нанесение изображения на ровную жёсткую основу (пенокартон, пластик)",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Сублимационная печать",
                'type': "services",
                'add_text': "перенос изображения на поверхность методом \"гравертон\"",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Сшивка",
                'type': "services",
                'add_text': "на скобу, пружину, нитку",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Тампопечать",
                'type': "services",
                'add_text': "печать на пластике",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Тиснение",
                'type': "services",
                'add_text': "одноуровневое или многоуровневое",
                'image': 'img/img-temp/400x270/img1.jpg'
            },
            {
                'name': "Фальцовка",
                'type': "services",
                'add_text': "формирование ровного изгиба",
                'image': 'img/img-temp/400x270/img1.jpg'
            }
        ]
        return context
