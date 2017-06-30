#include <stdio.h>
#include <string>
#include <iostream>

#include "data.h"

int main() {
    std::string date(11, ' '); // Data
    std::string time(9, ' '); // Horário
    float CO; // True hourly averaged concentration CO in mg/m^3
    int PT08S1; // tin oxide
    int NMHC; // Non Metanic HydroCarbons concentration in microg/m^3
    float C6H6; // Benzene concentration in microg/m^3
    int PT08S2; // titania
    int NOx; // NOx concentration in ppb
    int PT08S3; // tungsten oxide
    int NO2; // NO2 concentration in microg/m^3
    int PT08S4; // tungsten oxide
    int PT08S5; // indium oxide
    float T; // Temperature
    float RH; // Relative Humidity (%)
    float AH; // Absoulete Humidity

    int count = 0; // Contador de Teste
    while(scanf("%10s;%8s;%f;%d;%d;%f;%d;%d;%d;%d;%d;%d;%f;%f;%f;;",
                &date[0], &time[0], &CO, &PT08S1, &NMHC, &C6H6, &PT08S2, &NOx,
                &PT08S3, &NO2, &PT08S4, &PT08S5, &T, &RH, &AH) && count < 25){
        Data *data = new Data(date, time, CO, PT08S1, NMHC, C6H6, PT08S2, NOx,
                              PT08S3, NO2, PT08S4, PT08S5, T, RH, AH);
        data->print();
        count++;
    }
}
