    AsyncTask<Void, Void, String> task = new AsyncTask<Void, Void, String>() {
        @Override
        protected String doInBackground(Void... params) {
            AdvertisingIdClient.Info idInfo = null;
            try {
                idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
            } catch (GooglePlayServicesNotAvailableException e) {
                e.printStackTrace();
            } catch (GooglePlayServicesRepairableException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
            String advertId = null;
            try{
                advertId = idInfo.getId();
            }catch (NullPointerException e){
                e.printStackTrace();
            }

            return advertId;
        }

        @Override
        protected void onPostExecute(String advertId) {
            Toast.makeText(getApplicationContext(), advertId, Toast.LENGTH_SHORT).show();
        }

    };
    task.execute();
