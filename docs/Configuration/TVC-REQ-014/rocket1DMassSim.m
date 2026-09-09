%Assumptions
%- Only 1D
%- Fully vertical flight
%- Simplified friction from launch rail

g = 9.81;

frictionCoefficient = 0.2; %Low-end value of nylon/rubber on aluminum, assuming rail has been lubed by team

rocketParameters = readcell('RocketParameters.csv');

thrusts = cell2mat(rocketParameters(2:end,3)); %Newtons
times = cell2mat(rocketParameters(2:end,1)); %Seconds
motorMasses = cell2mat(rocketParameters(2:end,2)); %Grams
airPressures = cell2mat(rocketParameters(2:end,6)); %Pascals
airTemperature = cell2mat(rocketParameters(2:end,5)); %Kelvin
cD = cell2mat(rocketParameters(2:end,4));

R = 287.058; %Gas constant, J/(kg*k)

airDensities = airPressures ./ (R.* airTemperature); %kg

thrustLostFromGimbaling = 5; %Degrees, gives us worst case scenario where we lose some vertical thrust to gimbaling


maxCrossSection = 7.54767635025; %in^2
maxCrossSection = maxCrossSection ./ 1550; %Convert to meters^2

massRocket = 1050; %grams

%Initial Conditions
v = 0;

y = 0;

a = 0;

altitudes = y;
velocities = v;
accelerations = a;

for i = 1:length(times)-1
    totalMass = massRocket + motorMasses(i); %grams + grams
    totalMass = totalMass ./ 1000; %Convert to kg
    dragForce = 0.5*airDensities(i)*(v^2)*cD(i)*maxCrossSection; %kg/m^3 * m^2/s^2 * m^2 = kg*m/s^2 = N
    gravity = totalMass * g;

    %Friction from launch rail
    if y < 10 %till end of rail, ~10 m
        normalForce = thrusts(i) * sind(thrustLostFromGimbaling); %assume side force comes from a misaligned gimbal. This seems like an inaccurate way of calculating friction, would like to explore better methods
        frictionForce = normalForce * frictionCoefficient * 2; %Scaling using a binding coefficient to account for likely binding between the rail and rocket. Scales with force
    end

    totalForce = thrusts(i)*cosd(thrustLostFromGimbaling) - dragForce - gravity - frictionForce; %kg*m/s^2 (N) - N
    a = totalForce/totalMass; %kg*m/s^2 / kg = m/s^2
    dt = times(i+1) - times(i);
    v0 = v;
    v = v + a*dt; %
    y = y + v0*dt + 0.5*a*(dt^2);
    altitudes = [altitudes, y];
    velocities = [velocities, v];
    accelerations = [accelerations, a];
end

close all

figure;
plot(times, velocities)
xlabel('Time (s)')
ylabel('Velocity (m/s)')

figure;
plot(times, altitudes)
xlabel('Time (s)')
ylabel('ALtitude (m)')

figure;
plot(times, accelerations)
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')

