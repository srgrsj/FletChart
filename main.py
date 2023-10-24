import flet as ft
from target import Target


class State:
    displaying_chart = Target(0, 0).generate_chart()


s = State()


def main(page: ft.Page):
    page.title = "Flight chart"

    dlg = ft.AlertDialog(
        title=ft.Text("It is necessary to enter numbers"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.update()

    def is_convertible_to_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def data_change(e):
        try:
            if is_convertible_to_float(angle_field.value) and is_convertible_to_float(speed_field.value):
                page.controls.remove(s.displaying_chart)
                s.displaying_chart = Target(float(angle_field.value), float(speed_field.value)).generate_chart()
                page.controls.insert(0, s.displaying_chart)
                page.update()
            else:
                open_dlg()
        except e:
            pass

    angle_field = ft.TextField(label="Угол", value="", text_align=ft.TextAlign.CENTER, width=200)
    speed_field = ft.TextField(label="Скорость", value="", text_align=ft.TextAlign.CENTER, width=200)
    update_button = ft.FilledButton(text="update", on_click=data_change)

    page.add(
        s.displaying_chart,
        ft.Column(
            [
                ft.Row(
                    [
                        speed_field,
                        angle_field,
                        update_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,

                )
            ],
            spacing=50
        )
    )


ft.app(main)
