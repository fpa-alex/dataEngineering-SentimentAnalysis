$NewTab = $psISE.PowerShellTabs.Add()
$NewTab.DisplayName = "NewTab"
sleep -m 160
$NewTab.Invoke({cd C:\ ; cls})

$outcome = powershell Invoke-Expression "docker run -p 5000:5000 webinterface"
$outcome

while true
do
	wget -q --spider http://localhost:5000
	if [ $? -eq 0 ]; then
		echo "Online"
		break
	else 
		echo "Offline"
		sleep 5
	fi
done

python ./webinterface/test_app_automated.py