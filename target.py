import numpy as np
import flet as ft


class Target:
    def __init__(self, angle, speed):
        self.angle = angle
        self.speed = speed

    def generate_chart(self):
        angle_rad = np.radians(self.angle)
        g = 9.81
        time_of_flight = (2 * self.speed * np.sin(angle_rad)) / g
        time = np.linspace(0, time_of_flight, num=100)
        horizontal_position = self.speed * np.cos(angle_rad) * time
        vertical_position = self.speed * np.sin(angle_rad) * time - (0.5 * g * time ** 2)

        data = [
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(horizontal_position[i], vertical_position[i]) for i in
                             range(len(time))],
                color=ft.colors.LIGHT_GREEN,
                stroke_width=2,
            )
        ]

        chart = ft.LineChart(
            data_series=data,
            border=ft.Border(
                bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
            ),
            left_axis=ft.ChartAxis(
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            min_x=0,
            min_y=0,
            max_x=10,
            max_y=10,
            expand=True,
        )

        return chart
