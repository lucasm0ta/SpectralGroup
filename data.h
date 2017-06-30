#include <iostream>

#define SS << ' ' <<

#ifndef DATA_H
#define DATA_H

typedef struct Data{
    std::string date; // Data
    std::string time; // Horário
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

    Data(const std::string &date_i, const std::string &time_i, float CO_i,
        int PT08S1_i, int NMHC_i, float C6H6_i, int PT08S2_i, int NOx_i,
        int PT08S3_i, int NO2_i, int PT08S4_i, int PT08S5_i, float T_i,
        float RH_i, float AH_i) :
        date(date_i), time(time_i), CO(CO_i), PT08S1(PT08S1_i), NMHC(NMHC_i),
        C6H6(C6H6_i), PT08S2(PT08S2_i), NOx(NOx_i), PT08S3(PT08S3_i),
        NO2(NO2_i), PT08S4(PT08S4_i), PT08S5(PT08S5_i), T(T_i), RH(RH_i),
        AH(AH_i)
    {}

    void print()
    {
        std::cout << '\t' << date << ' ' << time << ' ' << CO << ' ' << PT08S1
        << ' ' << NMHC << ' ' << C6H6 << ' ' << PT08S2 << ' ' << NOx << ' ' <<
        PT08S3 << ' ' << NO2 << ' ' << PT08S4 << ' ' << PT08S5 << ' ' << T
        << ' ' << RH << ' ' << AH << std::endl;
    }

}Data;

#endif // DATA_H
