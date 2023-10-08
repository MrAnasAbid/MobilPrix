import pickle

columns = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time']

with open("./models/LogReg.p", 'rb') as pickled:
    data = pickle.load(pickled)
    log_reg_model = data["Best_LogReg"]