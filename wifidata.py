WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
WifiInfo wifiInfo;

wifiInfo = wifiManager.getConnectionInfo();
if (wifiInfo.getSupplicantState() == SupplicantState.COMPLETED) {
    ssid = wifiInfo.getSSID();
}
