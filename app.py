from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from main import *

##ISSUE WITH TBL GLOBAL VAR - want to update tbldropdown list after first selection not before...
class MyApp(App):
    def query_tbls(self, instance, x):
        tbls = connection.execute(
            f"select DISTINCT(column_name) from Reports where report_title = '{x}'"
        ).fetchall()
        for [tbl] in tbls:
            tableBtn = Button(text=f"{tbl}", size_hint_y=None, height=50)
            tableBtn.bind(
                on_release=lambda tableBtn: table_dropdown.select(tableBtn.text)
            )
            table_dropdown.add_widget(tableBtn)

    def build(self):

        tbls = ()

        report_dropdown = DropDown()
        for [report] in connection.execute(
            "select DISTINCT(report_title) from Reports"
        ).fetchall():
            reportBtn = Button(text=f"{report}", size_hint_y=None, height=50)
            reportBtn.bind(
                on_release=lambda reportBtn: report_dropdown.select(reportBtn.text)
            )
            report_dropdown.add_widget(reportBtn)

        report_dropdownBtn = Button(
            text="Report Options", size_hint=(None, None), width=500
        )
        report_dropdownBtn.bind(on_release=report_dropdown.open)

        report_dropdown.bind(
            on_select=lambda instance, x: setattr(report_dropdownBtn, "text", x)
        )
        report_dropdown.bind(on_select=self.query_tbls)
        report_dropdown.bind(
            on_select=lambda instance, x: setattr(table_dropdownBtn, "text", "Tables")
        )

        table_dropdown = DropDown()

        table_dropdownBtn = Button(text="Waiting for Report...", size_hint=(None, None))
        table_dropdownBtn.bind(on_release=table_dropdown.open)

        column_dropdown = DropDown()

        filter_dropdown = DropDown()

        main_layout = BoxLayout()
        main_layout.add_widget(report_dropdownBtn)
        main_layout.add_widget(table_dropdownBtn)
        return main_layout


if __name__ == "__main__":
    MyApp().run()
