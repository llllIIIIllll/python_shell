#!/bin/sh

sudo apt-get install -y acpid

grep "^action=/etc/acpi/powerbtn.sh" /etc/acpi/events/powerbtn > /dev/null

if [ $? -eq 0 ]; then
    echo "Need add comment" && sed -i 's/action=\/etc\/acpi\/powerbtn.sh/#action=\/etc\/acpi\/powerbtn.sh/g' /etc/acpi/events/powerbtn
else
    echo "Already commented"
fi

grep "^action=/sbin/poweroff" /etc/acpi/events/powerbtn > /dev/null

if [ $? -eq 0 ]; then
    echo "Already added"
else
    echo "Adding!" && echo "action=/sbin/poweroff" >> /etc/acpi/events/powerbtn 
fi

systemctl restart acpid.service
