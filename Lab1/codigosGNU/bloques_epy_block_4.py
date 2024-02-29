import numpy as np
from gnuradio import gr

class StepGenerator(gr.sync_block):
    def __init__(self, step_value=1.0, sample_rate=32000):  # Ajusta la tasa de muestreo a 32k
        gr.sync_block.__init__(
            self,
            name='StepGenerator',
            in_sig=[],
            out_sig=[np.float32]
        )
        self.step_value = step_value
        self.change_point = 10 * sample_rate  # 10 segundos multiplicados por la tasa de muestreo

    def work(self, input_items, output_items):
        y = output_items[0]
        for i in range(len(y)):
            if i < self.change_point:
                y[i] = 0.0
            else:
                y[i] = self.step_value
        return len(y)

# Crear una instancia del bloque generador de señal de escalón
# Puedes cambiar el valor de 'step_value' según tus necesidades
my_step_generator = StepGenerator(step_value=1.0, sample_rate=32000)  # Ajusta la tasa de muestreo a 32k
