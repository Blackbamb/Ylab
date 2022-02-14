import math
from tkinter import *


class God:

    def __init__(self):
        self.window = Tk()
        self.window.title('Геометрический калькулятор')
        self.window.geometry("400x400")
        self.frame = LabelFrame(self.window, text="Ver.1")
        self.frame.pack(expand=True, fill=BOTH)
        self.lbl = Label(self.frame, text="Геометрический калькулятор \n Выберите:", font=("Times", 14))
        self.lbl.pack()
        self.btn1 = Button(self.frame, text="Плоские фигуры", font=("Times", 12), bg='#A877BA', command=self.click_flat)
        self.btn1.place(relx=0.1, rely=0.2)
        self.btn2 = Button(self.frame, text="Объемные фигуры", font=("Times", 12), bg='#54FA9B',
                           command=self.click_voluminous)
        self.btn2.place(relx=0.55, rely=0.2)

        self.circle = Button(self.frame, text="Круг", font=("Times", 12), bg='#A877BA', command=self.circle_math)
        self.square = Button(self.frame, text="Квадрат", font=("Times", 12), bg='#A877BA', command=self.square_math)
        self.rectangle = Button(self.frame, text="Прямоугольник", font=("Times", 12), bg='#A877BA',
                                command=self.rectangle_math)
        self.triangle = Button(self.frame, text="Треугольник", font=("Times", 12), bg='#A877BA',
                               command=self.triangle_math)
        self.trapezoid = Button(self.frame, text="Трапеция", font=("Times", 12), bg='#A877BA',
                                command=self.trapezoid_math)
        self.rhombus = Button(self.frame, text="Ромб", font=("Times", 12), bg='#A877BA', command=self.rhombus_math)

        self.sphere = Button(self.frame, text="Сфера", font=("Times", 12), bg='#54FA9B', command=self.sphere_math)
        self.cube = Button(self.frame, text="Куб", font=("Times", 12), bg='#54FA9B', command=self.cube_math)
        self.parallelepiped = Button(self.frame, text="Параллелепипед", font=("Times", 12), bg='#54FA9B',
                                     command=self.parallelepiped_math)
        self.pyramid = Button(self.frame, text="Пирамида", font=("Times", 12), bg='#54FA9B', command=self.pyramid_math)
        self.cylinder = Button(self.frame, text="Цилиндр", font=("Times", 12), bg='#54FA9B', command=self.cylinder_math)
        self.cone = Button(self.frame, text="Конус", font=("Times", 12), bg='#54FA9B', command=self.cone_math)

        self.back1 = Button(self.frame, text="Назад", font=("Times", 12), bg='red', command=self.first)
        self.back2 = Button(self.frame, text="Назад", font=("Times", 12), bg='red', command=self.second)
        self.back3 = Button(self.frame, text="Назад", font=("Times", 12), bg='red', command=self.third)
        self.back4 = Button(self.frame, text="Назад", font=("Times", 12), bg='red', command=self.four)

        self.dist1 = [self.circle, self.square, self.rectangle, self.triangle, self.trapezoid, self.rhombus]
        self.dist2 = [self.sphere, self.cube, self.parallelepiped, self.pyramid, self.cylinder, self.cone]

        self.x = Label(self.frame, text="x=", font=("Times", 14))
        self.y = Label(self.frame, text="y=", font=("Times", 14))

        self.window.mainloop()

    def click_flat(self):
        for i in self.dist1:
            i.pack(fill=X)
        self.btn1.destroy()
        self.btn2.destroy()
        self.back_home(self.back1)

    def click_voluminous(self):
        for i in self.dist2:
            i.pack(fill=X)
        self.btn1.destroy()
        self.btn2.destroy()
        self.back_home(self.back2)

    def back_home(self, back):
        self.back = back
        self.back.pack(side=BOTTOM, fill=X)

    def first(self):
        for i in self.dist1:
            i.pack_forget()
        self.back1.pack_forget()
        self.btn1 = Button(self.frame, text="Плоские фигуры", font=("Times", 12), bg='#A877BA', command=self.click_flat)
        self.btn1.place(relx=0.1, rely=0.2)
        self.btn2 = Button(self.frame, text="Объемные фигуры", font=("Times", 12), bg='#54FA9B',
                           command=self.click_voluminous)
        self.btn2.place(relx=0.55, rely=0.2)

    def second(self):
        for i in self.dist2:
            i.pack_forget()
        self.back2.pack_forget()
        self.btn1 = Button(self.frame, text="Плоские фигуры", font=("Times", 12), bg='#A877BA', command=self.click_flat)
        self.btn1.place(relx=0.1, rely=0.2)
        self.btn2 = Button(self.frame, text="Объемные фигуры", font=("Times", 12), bg='#54FA9B',
                           command=self.click_voluminous)
        self.btn2.place(relx=0.55, rely=0.2)

    def third(self):
        pass

    def four(self):
        pass

    def des_1(self):
        for i in self.dist1:
            i.pack_forget()
        self.back1.pack_forget()
        self.lbl.pack_forget()

    def des_2(self):
        for i in self.dist2:
            i.pack_forget()
        self.back2.pack_forget()
        self.lbl.pack_forget()

    def circle_math(self):
        pass

    def square_math(self):
        pass

    def rectangle_math(self):
        pass

    def triangle_math(self):
        pass

    def trapezoid_math(self):
        pass

    def rhombus_math(self):
        pass

    def sphere_math(self):
        pass

    def cube_math(self):
        pass

    def parallelepiped_math(self):
        pass

    def pyramid_math(self):
        pass

    def cylinder_math(self):
        pass

    def cone_math(self):
        pass

    def image(self, t, e, m, r, k, x1, x2):
        self.sq = Label(self.frame, text=f"{t}", font=("Times", 14))
        self.img = PhotoImage(file=f"image\{t}.png").subsample(m, m)
        self.label = Label(self.frame, image=self.img)
        self.label.image_ref = self.img
        self.label.place(relx=r, rely=k)
        God.x(self, e, x1, x2)

    def x(self, x, x1, x2):
        self.x = Label(self.frame, text=f"{x}", font=("Times", 14))
        self.x.place(rely=x2, relx=x1)
        self.plo = Label(self.frame, text=f"S=", font=("Times", 14))
        self.plo.place(rely=0.4, relx=0.7)
        self.p = Label(self.frame, font=("Times", 14))
        self.p.place(rely=0.4, relx=0.78)
        self.ent_x = Entry(self.frame, width=5, font=14)
        self.ent_x.place(rely=0.305, relx=0.78)
        self.ok = Button(self.frame, text="Ok!", font=("Times", 12), bg='red', command=self.get)
        self.fig = Label(self.frame, font=("Times", 14))

    def y(self, y, x1, y1, x2, y2):
        self.y = Label(self.frame, text=f"{y}", font=("Times", 14))
        self.y.place(relx=x1, rely=y1)
        self.fig1 = Label(self.frame, font=("Times", 14))
        self.fig1.place(relx=x2, rely=y2)
        self.ent_y = Entry(self.frame, width=5, font=14)
        self.ent_y.place(rely=0.205, relx=0.78)

    def z(self, y, x1, y1, x2, y2):
        self.z = Label(self.frame, text=f"{y}", font=("Times", 14))
        self.z.place(relx=x1, rely=y1)
        self.fig2 = Label(self.frame, font=("Times", 14))
        self.fig2.place(relx=x2, rely=y2)
        self.ent_z = Entry(self.frame, width=5, font=14)
        self.ent_z.place(rely=0.105, relx=0.78)

    def get(self):
        if self.sq['text'] == 'Круг' or self.sq['text'] == 'Квадрат' or self.sq['text'] == 'Сфера' or \
                self.sq['text'] == 'Куб':
            self.fig['text'] = self.ent_x.get()
        elif self.sq['text'] == 'Прямоугольник' or self.sq['text'] == 'Ромб' or self.sq['text'] == 'Пирамида' or \
                self.sq['text'] == 'Цилиндр' or self.sq['text'] == 'Конус':
            self.fig['text'] = self.ent_x.get()
            self.fig1['text'] = self.ent_y.get()
        elif self.sq['text'] == 'Треугольник' or self.sq['text'] == 'Трапеция' or self.sq['text'] == 'Параллелепипед':
            self.fig['text'] = self.ent_x.get()
            self.fig1['text'] = self.ent_y.get()
            self.fig2['text'] = self.ent_z.get()


class Krug(God):
    def get(self):
        super().get()
        if self.sq['text'] == 'Круг':
            r = float(self.ent_x.get())
            self.p['text'] = Krug.pl(r)

    def circle_math(self):
        self.des_1()
        God.image(self, 'Круг', 'r=', 4, 0, 0.1, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.3, relx=0.35)

    def third(self):
        self.back_home(self.back1)
        self.lbl.pack()
        for i in self.dist1:
            i.pack(fill=X)
        self.p.destroy()
        self.plo.destroy()
        self.x.destroy()
        self.ent_x.destroy()
        self.ok.destroy()
        self.fig.destroy()
        self.label.destroy()
        self.back3.pack_forget()
        self.sq.pack_forget()

    @staticmethod
    def pl(x):
        a = x ** 2 * math.pi
        return round(a, 3)


class Kvad(Krug):
    def get(self):
        super().get()
        if self.sq['text'] == 'Квадрат':
            a = float(self.ent_x.get())
            self.p['text'] = Kvad.pl_kv(a)

    def square_math(self):
        self.des_1()
        God.image(self, 'Квадрат', 'x=', 1, 0, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.15, relx=0.25)

    @classmethod
    def pl_kv(cls, x):
        return round(x ** 2, 3)


class Sfera(Kvad):
    def get(self):
        super().get()
        if self.sq['text'] == 'Сфера':
            r = float(self.ent_x.get())
            self.p['text'] = 4 * Krug.pl(r)

    def sphere_math(self):
        self.des_2()
        God.image(self, 'Сфера', 'r=', 1, 0, 0.1, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.43, relx=0.2)

    def four(self):
        self.back_home(self.back2)
        self.lbl.pack()
        for i in self.dist2:
            i.pack(fill=X)
        self.p.destroy()
        self.plo.destroy()
        self.x.destroy()
        self.ent_x.destroy()
        self.ok.destroy()
        self.fig.destroy()
        self.label.destroy()
        self.back4.pack_forget()
        self.sq.pack_forget()


class Kub(Sfera):
    def get(self):
        super().get()
        if self.sq['text'] == 'Куб':
            a = float(self.ent_x.get())
            self.p['text'] = 6 * Kvad.pl_kv(a)

    def cube_math(self):
        self.des_2()
        God.image(self, 'Куб', 'x=', 1, 0, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.6, relx=0.47)


class Prm(Kub):
    def get(self):
        super().get()
        if self.sq['text'] == 'Прямоугольник':
            a = float(self.ent_x.get())
            b = float(self.ent_y.get())
            self.p['text'] = Prm.pl_prym(a, b)

    def rectangle_math(self):
        self.des_1()
        God.image(self, 'Прямоугольник', 'y=', 1, 0, 0.27, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.2, relx=0.28)
        God.y(self, 'x=', 0.7, 0.2, 0.6, 0.44)

    def third(self):
        super().third()
        if self.sq['text'] != "Круг" and self.sq['text'] != "Квадрат":
            self.y.destroy()
            self.ent_y.destroy()
            self.fig1.destroy()

    @staticmethod
    def pl_prym(a, b):
        return a * b


class Romb(Prm):
    def get(self):
        super().get()
        if self.sq['text'] == 'Ромб':
            a = float(self.ent_x.get())
            b = float(self.ent_y.get())
            self.p['text'] = Prm.pl_prym(a, b) / 2

    def rhombus_math(self):
        self.des_1()
        God.image(self, 'Ромб', 'BD=', 4, 0, 0.1, 0.675, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.37, relx=0.35)
        God.y(self, 'AC=', 0.675, 0.2, 0.28, 0.3)


class Piramida(Romb):
    def get(self):
        super().get()
        if self.sq['text'] == 'Пирамида':
            a = float(self.ent_y.get())
            b = float(self.ent_x.get())
            self.p['text'] = round((a ** 2 * math.sqrt(3) + 6 * a * math.sqrt(b ** 2 - a ** 2 / 4)) / 4, 3)

    def pyramid_math(self):
        self.des_2()
        God.image(self, 'Пирамида', 'b=', 4, 0, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.4, relx=0.5)
        God.y(self, 'a=', 0.7, 0.2, 0.48, 0.72)

    def four(self):
        super().four()
        if self.sq['text'] != "Сфера" and self.sq['text'] != "Куб":
            self.y.destroy()
            self.ent_y.destroy()
            self.fig1.destroy()


class Cilindr(Piramida):
    def get(self):
        super().get()
        if self.sq['text'] == 'Цилиндр':
            r = float(self.ent_y.get())
            h = float(self.ent_x.get())
            self.p['text'] = round(2 * math.pi * r * (r + h), 3)

    def cylinder_math(self):
        self.des_2()
        God.image(self, 'Цилиндр', 'h=', 2, 0.2, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.44, relx=0.4)
        God.y(self, 'r=', 0.7, 0.2, 0.42, 0.595)


class Konus(Cilindr):
    def get(self):
        super().get()
        if self.sq['text'] == 'Конус':
            r = float(self.ent_y.get())
            h = float(self.ent_x.get())
            self.p['text'] = round(math.pi * r * math.sqrt(r ** 2 + h ** 2) + Krug.pl(r), 3)

    def cone_math(self):
        self.des_2()
        God.image(self, 'Конус', 'h=', 2, 0.2, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.44, relx=0.37)
        God.y(self, 'r=', 0.7, 0.2, 0.42, 0.595)


class Treug(Konus):
    def get(self):
        super().get()
        if self.sq['text'] == 'Треугольник':
            a = float(self.ent_x.get())
            b = float(self.ent_y.get())
            c = float(self.ent_z.get())
            p = (a + b + c) / 2
            if p * (p - a) * (p - b) * (p - c) >= 0:
                self.p['text'] = round(Treug.area(a, b, c, p), 3)
            else:
                self.p['text'] = "does't exist"

    def triangle_math(self):
        self.des_1()
        God.image(self, 'Треугольник', 'z=', 3, 0.1, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.67, relx=0.3)
        God.y(self, 'y=', 0.7, 0.2, 0.415, 0.3)
        God.z(self, 'x=', 0.7, 0.1, 0.2, 0.3)

    def third(self):
        super().third()
        if self.sq['text'] != "Круг" and self.sq['text'] != "Квадрат" and self.sq['text'] != "Прямоугольник" and self.sq['text'] != "Ромб":
            self.z.destroy()
            self.ent_z.destroy()
            self.fig2.destroy()

    @staticmethod
    def area(a, b, c, p):
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Trap(Treug):
    def get(self):
        super().get()
        if self.sq['text'] == 'Трапеция':
            a = float(self.ent_z.get())
            b = float(self.ent_y.get())
            h = float(self.ent_x.get())
            self.p['text'] = round(h * (a + b) / 2, 3)

    def trapezoid_math(self):
        self.des_1()
        God.image(self, 'Трапеция', 'h=', 5, 0, 0.25, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back3)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.4, relx=0.1)
        God.y(self, 'c=', 0.7, 0.2, 0.25, 0.23)
        God.z(self, 'a=', 0.7, 0.1, 0.3, 0.6)


class Parall(Trap):
    def get(self):
        super().get()
        if self.sq['text'] == 'Параллелепипед':
            a = float(self.ent_z.get())
            b = float(self.ent_y.get())
            c = float(self.ent_x.get())
            self.p['text'] = round(2 * (a * b + a * c + b * c), 3)

    def parallelepiped_math(self):
        self.des_2()
        God.image(self, 'Параллелепипед', 'c=', 3, 0, 0.2, 0.7, 0.3)
        self.sq.pack()
        self.back_home(self.back4)
        self.ok.place(rely=0.5, relx=0.7)
        self.fig.place(rely=0.4, relx=0.48)
        God.y(self, 'b=', 0.7, 0.2, 0.59, 0.53)
        God.z(self, 'a=', 0.7, 0.1, 0.28, 0.59)

    def four(self):
        super().four()
        if self.sq['text'] != "Сфера" and self.sq['text'] != "Куб" and self.sq['text'] != "Пирамида" \
                and self.sq['text'] != "Цилиндр" and self.sq['text'] != "Конус":
            self.z.destroy()
            self.ent_z.destroy()
            self.fig2.destroy()


class Medianapiramida(Parall):

    def pyramid_math(self):
        super().pyramid_math()
        if self.sq['text'] == "Пирамида":
            Medianapiramida.z(self, 'L=', 0.7, 0.7, 0.43, 0.5)
            self.ent_z.destroy()
            self.en = Label(self.frame, font=("Times", 14))
            self.en.place(relx=0.78, rely=0.7)

    def get(self):
        super().get()
        if self.sq['text'] == "Пирамида":
            a = float(self.ent_y.get())
            b = float(self.ent_x.get())
            self.en['text'] = self.fig2['text'] = round(math.sqrt(b ** 2 - (a / 2) ** 2), 3)

    def four(self):
        super().four()
        if self.sq['text'] == "Пирамида":
            self.en.destroy()
            self.z.destroy()
            self.fig2.destroy()
