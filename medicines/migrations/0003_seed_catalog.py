from django.db import migrations


def seed_catalog(apps, schema_editor):
    Category = apps.get_model("medicines", "Category")
    Medicine = apps.get_model("medicines", "Medicine")

    categories = {
        name: Category.objects.create(name=name, description=description)
        for name, description in [
            ("Pain Relief", "Medicines for everyday pain and fever relief."),
            ("Cold & Flu", "Support for common cold and flu symptoms."),
            ("Skin Care", "Creams and ointments for common skin concerns."),
            ("First Aid", "Essential supplies for minor injuries."),
            ("Diabetes Care", "Products to support diabetes management."),
            ("Heart Health", "Products for everyday cardiovascular care."),
        ]
    }

    medicines = [
        ("Paracetamol 500mg", "Pain and fever relief tablets.", "Pain Relief", "49.00", 100),
        ("Ibuprofen 200mg", "Anti-inflammatory pain relief tablets.", "Pain Relief", "79.00", 80),
        ("Cough Relief Syrup", "Syrup for temporary cough relief.", "Cold & Flu", "125.00", 60),
        ("Cold Relief Tablets", "Relief for common cold symptoms.", "Cold & Flu", "99.00", 75),
        ("Antiseptic Cream", "Cream for minor cuts and grazes.", "Skin Care", "89.00", 50),
        ("Moisturizing Ointment", "Moisturizing ointment for dry skin.", "Skin Care", "149.00", 45),
        ("Adhesive Bandages", "Sterile bandages for minor wounds.", "First Aid", "39.00", 120),
        ("Digital Thermometer", "Fast and accurate temperature readings.", "First Aid", "299.00", 35),
        ("Glucose Test Strips", "Test strips for compatible glucose meters.", "Diabetes Care", "499.00", 40),
        ("Sugar-Free Cough Syrup", "Sugar-free syrup for cough relief.", "Diabetes Care", "159.00", 30),
        ("Omega 3 Capsules", "Daily supplement for general heart health.", "Heart Health", "349.00", 55),
        ("Blood Pressure Monitor", "Digital monitor for home blood pressure checks.", "Heart Health", "1299.00", 20),
    ]

    Medicine.objects.bulk_create(
        [
            Medicine(
                name=name,
                description=description,
                category=categories[category],
                price=price,
                stock=stock,
                is_active=True,
            )
            for name, description, category, price, stock in medicines
        ]
    )


def remove_catalog(apps, schema_editor):
    Medicine = apps.get_model("medicines", "Medicine")
    Category = apps.get_model("medicines", "Category")
    Medicine.objects.filter(name__in=[
        "Paracetamol 500mg",
        "Ibuprofen 200mg",
        "Cough Relief Syrup",
        "Cold Relief Tablets",
        "Antiseptic Cream",
        "Moisturizing Ointment",
        "Adhesive Bandages",
        "Digital Thermometer",
        "Glucose Test Strips",
        "Sugar-Free Cough Syrup",
        "Omega 3 Capsules",
        "Blood Pressure Monitor",
    ]).delete()
    Category.objects.filter(name__in=[
        "Pain Relief",
        "Cold & Flu",
        "Skin Care",
        "First Aid",
        "Diabetes Care",
        "Heart Health",
    ]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0002_searchlog_alter_category_id_alter_medicine_id"),
    ]

    operations = [
        migrations.RunPython(seed_catalog, remove_catalog),
    ]
