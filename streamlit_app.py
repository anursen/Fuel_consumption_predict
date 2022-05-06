import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def calculate_mpg(actual_mpg,velocity):
  mpg = (-0.00062 * actual_mpg**2 + 0.01345*actual_mpg - 0.34192) * velocity + 0.0533*actual_mpg**2 - 0.3580* actual_mpg + 30.0424 
  return mpg

def calculate_cost_of_travel_time(hourly_rate,distance,mph):
  travel_time = distance/mph
  return hourly_rate * travel_time


def calc_gas_cost(total_distance,mpg,gas_price=4,):
  return total_distance / mpg * gas_price

st.title('Crusing Speed Affects Your Fuel Consumption, But How Much?')


Distance_to_work = st.slider('Travel Distance',0, 100, 1)
Gas_Price = st.slider('Gas Price',0.0,10.0, 4.1)
Hourly_rate = st.slider('Hourly Salary or Opportunity Cost', 0, 100, 13)
Cars_mpg = st.slider('Your Cars Mpg', 5, 100, 19)

speed_series = np.linspace(55,90,50)
mpg_series = calculate_mpg(Cars_mpg,speed_series)
cost_series = calculate_cost_of_travel_time(Hourly_rate,Distance_to_work,speed_series) + calc_gas_cost(Distance_to_work,mpg_series)
cost_of_time_series = calculate_cost_of_travel_time(Hourly_rate,Distance_to_work,mpg_series)

result = round(float(speed_series[np.where(cost_series == cost_series.min())]),2)
st.write('Your optimum travel speed is: ',result)


fig, ax = plt.subplots()
ax.plot(speed_series,cost_series)

plt.title("Speed vs Cost perMile")
plt.xlabel("Speed")
plt.ylabel("Cost perMile")
plt.grid()

st.pyplot(fig)


