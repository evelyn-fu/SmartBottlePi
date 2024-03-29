const bleno = require('bleno');

const BASE_UUID = '-5659-402b-aeb3-d2f7dcd1b999';
const PERIPHERAL_ID = '0000';
const PRIMARY_SERVICE_ID = '0100';

var primary_service_uuid = PERIPHERAL_ID + PRIMARY_SERVICE_ID + BASE_UUID;
var ps_characteristic_uuid = PERIPHERAL_ID + '0300' + BASE_UUID; 

var settings = {
service_id: primary_service_uuid,
characteristic_id: ps_characteristic_uuid
};

bleno.on('stateChange', function(state){
if(state === 'poweredOn'){
bleno.startAdvertising('AttendanceApp', [settings.service_id]);
}else{
bleno.stopAdvertising();
}
});

 bleno.on('advertisingStart', function(error){
        if(error){
          console.log('something went wrong while trying to start advertisement of services');
        }else{
          console.log('started..');
          bleno.setServices([
            new bleno.PrimaryService({ // create a service
              uuid : settings.service_id,
              characteristics : [
                new bleno.Characteristic({ // add a characteristic to the service
                  value : null,
                  uuid : settings.characteristic_id,
                  properties : ['write'],
                  onWriteRequest : function(data, offset, withoutResponse, callback){

                    // next: add code for processing write request
                  }
                })
              ]
            })
          ]);
        }
    });

 bleno.on('accept', function(clientAddress){
      console.log('client address: ', clientAddress);
      var data = {
        is_attendees: true,
        attendees: attendees
      };
      console.log("accepted");
    });