class FigureAkinator:

    figure = None

    class Type:
        CIRCLE = 'circle'
        SQUARE = 'square'
        TRIANGLE = 'triangle'
        RECTANGLE = 'rectangle'
        PARALLELOGRAM = 'parallelogram'

    def start(self):
        self.figure = self.think()

        if self.figure:
            print('Ура! Давай узнаем ее площадь!')

            print(self.__dict__)

            result = getattr(self, f'get_space_of_{self.figure}')()

            print(f'Площадь фигуры: {result}')


    def think(self):
        print('Загадайте фигуру и отвечайте на вопросы.')

        is_angles = input('У фигуры есть углы? (да/нет): ') == 'да'

        if not is_angles:
            is_circle = input('Фигура является кругом? (да/нет): ') == 'да'

            if not is_circle: return None

            return self.Type.CIRCLE
        
        else:
            is_parallel = input('У фигуры есть параллельные стороны? (да/нет): ') == 'да'
            if is_parallel:
                is_direct_angle = input('У фигуры есть прямые углы? (да/нет): ') == 'да'
                
                if is_direct_angle:
                    is_equialsides = input('У фигуры все стороны равны? (да/нет): ') == 'да'
                    

                    if is_equialsides:
                        is_square = input('Фигура является квадратом? (да/нет): ') == 'да'

                        if not is_square: return None
                        else: return self.Type.SQUARE
                
                    else:
                        is_rectangle = input('Фигура является прямоугольником? (да/нет): ') == 'да'

                        if not is_rectangle: return None
                        else: return self.Type.RECTANGLE
                            
                else:
                    is_parallelogram = input('Фигура является параллелограмом? (да/нет): ') == 'да'

                    if not is_parallelogram: return None
                    else: return self.Type.PARALLELOGRAM
                    
        return None
    

    def get_space_of_circle(self):
        r = float(input('Введите радиус круга: '))

        return 3.14*r**2
    
    def get_space_of_square(self):
        a = float(input('Введите длину стороны квадрата: '))

        return a**2
    
    def get_space_of_rectangle(self):
        a = float(input('Введите длину стороны прямоугольника: '))
        b = float(input('Введите ширину стороны прямоугольника: '))

        return a * b

    def get_space_of_parallelogram(self):
        a = float(input('Введите основание параллелограмма: '))
        h = float(input('Введите высоту параллелограмма: '))

        return a*h
    

AkinatorManager = FigureAkinator()

AkinatorManager.start()