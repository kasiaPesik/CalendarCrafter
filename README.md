Documentation / Dokumentacja
Project Name / Nazwa Projektu: CalendarCrafter
Description / Opis:
The CalendarCrafter project is a simple application that allows users to retrieve and save public holidays data for a selected country and year. The application is built using Python and the Tkinter library for the graphical user interface.

Projekt CalendarCrafter to prosta aplikacja umożliwiająca użytkownikom pobieranie i zapisywanie danych dotyczących świąt publicznych dla wybranego kraju i roku. Aplikacja została zbudowana przy użyciu języka Python oraz biblioteki Tkinter do interfejsu graficznego użytkownika.

How to Use / Jak korzystać:
Launch the application by running the provided code.

Uruchom aplikację, uruchamiając dostarczony kod.
Enter the necessary information:

Wybierz kraj z listy rozwijanej ("Select country").
Wprowadź rok w polu "Year".
Wybierz format pliku (CSV lub XLSX) z listy rozwijanej "File extension".
Click the "Run app" button to retrieve and save public holidays data.

Kliknij przycisk "Run app", aby pobrać i zapisać dane dotyczące świąt publicznych.
The results will be saved in the "Output" folder as a CSV or XLSX file, depending on the selected format.

Wyniki zostaną zapisane w folderze "Output" jako plik CSV lub XLSX, w zależności od wybranego formatu.
Dependencies / Zależności:
pandas
requests
customtkinter
tkinter
API Used / Użyte API:
The application uses the "Nager Date" API to retrieve public holidays data.
Aplikacja korzysta z API "Nager Date" do pobierania danych dotyczących świąt publicznych.

API URL: https://date.nager.at/api/v2/PublicHolidays
File Output / Wyjście plikowe:
The output file is saved in the "Output" folder with a filename format: "Holiday [country_code] [year].[file_extension]".
Plik wynikowy jest zapisywany w folderze "Output" z formatem nazwy pliku: "Holiday [kod_kraju] [rok].[rozszerzenie_pliku]".

Error Handling / Obsługa błędów:
If the user fails to provide required information (country, year, or file extension), warning messages will be displayed.

Jeśli użytkownik nie poda wymaganych informacji (kraj, rok lub rozszerzenie pliku), zostaną wyświetlone komunikaty ostrzegawcze.
If an error occurs during the API request or data processing, an error message will be displayed.

Jeśli wystąpi błąd podczas żądania API lub przetwarzania danych, zostanie wyświetlony komunikat błędu.
Customization / Dostosowywanie:
The application's appearance is customized using the customtkinter library, with a white theme and blue color accents.
Wygląd aplikacji został dostosowany przy użyciu biblioteki customtkinter, z białym motywem i akcentami koloru niebieskiego.
