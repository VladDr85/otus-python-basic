class TestContacts:
    def test_get_id_contact_full(self, contact_full):
        assert contact_full.get_id() == 1

    def test_get_id_contact_empty(self, contact_empty):
        assert contact_empty.get_id() == 1

    def test_get_name_contact_full(self, contact_full, get_test_contact):
        assert contact_full.get_name() == get_test_contact['name']

    def test_get_name_contact_empty(self, contact_empty):
        assert contact_empty.get_name() == ''

    def test_get_phone_contact_full(self, contact_full, get_test_contact):
        assert contact_full.get_phone() == get_test_contact['phone']

    def test_get_phone_contact_empty(self, contact_empty):
        assert contact_empty.get_phone() == ''

    def test_get_mail_contact_full(self, contact_full, get_test_contact):
        assert contact_full.get_mail() == get_test_contact['mail']

    def test_get_mail_contact_empty(self, contact_empty):
        assert contact_empty.get_mail() == ''

    def test_get_status_contact_full(self, contact_full, get_test_contact):
        assert contact_full.get_status() == get_test_contact['status']

    def test_get_status_contact_empty(self, contact_empty):
        assert contact_empty.get_status() == ''

    def test_get_city_contact_full(self, contact_full, get_test_contact):
        assert contact_full.get_city() == get_test_contact['city']

    def test_get_city_contact_empty(self, contact_empty):
        assert contact_empty.get_city() == ''

    def test_get_contact(self, contact_full, get_test_contact):
        assert contact_full.get_contact() == get_test_contact

    def test_set_name_contact_full(self, contact_full):
        contact_full.set_name('Толян')
        assert contact_full.get_name() == 'Толян'

    def test_set_phone_contact_full(self, contact_full):
        contact_full.set_phone('+123-456-789')
        assert contact_full.get_phone() == '+123-456-789'

    def test_set_mail_contact_full(self, contact_full):
        contact_full.set_mail('ya_tolyan@yaho.com')
        assert contact_full.get_mail() == 'ya_tolyan@yaho.com'

    def test_set_status_contact_full(self, contact_full):
        contact_full.set_status('Приятель друга')
        assert contact_full.get_status() == 'Приятель друга'

    def test_set_city_contact_full(self, contact_full):
        contact_full.set_city('New York City')
        assert contact_full.get_city() == 'New York City'
