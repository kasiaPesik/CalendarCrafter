<h2>Project Name / Nazwa Projektu: CalendarCrafter</h2>

<h3>Description / Opis:</h3>
<p>The CalendarCrafter project is a simple application that allows users to retrieve and save public holidays data for a selected country and year. The application is built using Python and the Tkinter library for the graphical user interface.</p>

<p>Projekt CalendarCrafter to prosta aplikacja umożliwiająca użytkownikom pobieranie i zapisywanie danych dotyczących świąt publicznych dla wybranego kraju i roku. Aplikacja została zbudowana przy użyciu języka Python oraz biblioteki Tkinter do interfejsu graficznego użytkownika.</p>

<h3>How to Use / Jak korzystać:</h3>
<ol>
    <li>Launch the application by running the provided code.
        <ul>
            <li>Uruchom aplikację, uruchamiając dostarczony kod.</li>
        </ul>
    </li>
    <li>Enter the necessary information:
        <ul>
            <li>Wybierz kraj z listy rozwijanej ("Select country").</li>
            <li>Wprowadź rok w polu "Year".</li>
            <li>Wybierz format pliku (CSV lub XLSX) z listy rozwijanej "File extension".</li>
        </ul>
    </li>
    <li>Click the "Run app" button to retrieve and save public holidays data.
        <ul>
            <li>Kliknij przycisk "Run app", aby pobrać i zapisać dane dotyczące świąt publicznych.</li>
        </ul>
    </li>
    <li>The results will be saved in the "Output" folder as a CSV or XLSX file, depending on the selected format.
        <ul>
            <li>Wyniki zostaną zapisane w folderze "Output" jako plik CSV lub XLSX, w zależności od wybranego formatu.</li>
        </ul>
    </li>
</ol>

<h3>Dependencies / Zależności:</h3>
<ul>
    <li>pandas</li>
    <li>requests</li>
    <li>customtkinter</li>
    <li>tkinter</li>
</ul>

<h3>API Used / Użyte API:</h3>
<p>The application uses the "Nager Date" API to retrieve public holidays data.
Aplikacja korzysta z API "Nager Date" do pobierania danych dotyczących świąt publicznych.</p>

<p>API URL: <a href="https://date.nager.at/api/v2/PublicHolidays">https://date.nager.at/api/v2/PublicHolidays</a></p>

<h3>File Output / Wyjście plikowe:</h3>
<p>The output file is saved in the "Output" folder with a filename format: <code>Holiday [country_code] [year].[file_extension]</code>.
Plik wynikowy jest zapisywany w folderze "Output" z formatem nazwy pliku: <code>Holiday [kod_kraju] [rok].[rozszerzenie_pliku]</code>.</p>

<h3>Error Handling / Obsługa błędów:</h3>
<ul>
    <li>If the user fails to provide required information (country, year, or file extension), warning messages will be displayed.
        <ul>
            <li>Jeśli użytkownik nie poda wymaganych informacji (kraj, rok lub rozszerzenie pliku), zostaną wyświetlone komunikaty ostrzegawcze.</li>
        </ul>
    </li>
    <li>If an error occurs during the API request or data processing, an error message will be displayed.
        <ul>
            <li>Jeśli wystąpi błąd podczas żądania API lub przetwarzania danych, zostanie wyświetlony komunikat błędu.</li>
        </ul>
    </li>
</ul>

<h3>Customization / Dostosowywanie:</h3>
<p>The application's appearance is customized using the customtkinter library, with a white theme and blue color accents.
Wygląd aplikacji został dostosowany przy użyciu biblioteki customtkinter, z białym motywem i akcentami koloru niebieskiego.</p>

<h3>Author / Autor:</h3>
<p>[Your Name or Username]</p>

<h3>Date / Data:</h3>
<p>[Date of Documentation Creation]</p>

</body>
</html>
