# Jak vytvořit Registraci uživatelů

## V které sekci založit HTML soubor

- Registrace řešena
- nav/template - hlavní ikony

1.6 Contact:
- Aktualizujeme sablonu base.html aby měla odkaz na "Contact"
- Vytvořit šablonu contact.html a contact_detail.html, která bude zobrazovat kontakty
- Změňit odkaz na stránku "Contact" tak, aby směřoval na správnou URL v nav.html: <a class="nav-item nav-link active" href="{% url 'contact' %}">Contact</a>
- Definujeme funkce def contact a def contact_detail do views.py
- Přidáme cestu pro contact do urls.py: path('contact/', contact, name='contact'),

1.7 Edit:

- Vytvoření nové šablony edit_event.html pro formulář úpravy událostí.
- Přidání tlačítka pro úpravu událostí pouze pro administratora v event_detail.html: 
- Definujeme funkci def edit_event(request, event_id): ve views.py
- Přidáme cestu pro editaci udalosti do urls.py:  path('event/<int:event_id>/edit/', edit_event, name='edit_event'),



