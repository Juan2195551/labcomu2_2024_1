import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self, start=0, step=1):
        gr.sync_block.__init__(
            self,
            name='e_ACUM',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.value = start
        self.step = step

    def work(self, input_items, output_items):
        y = output_items[0]
        for i in range(len(y)):
            y[i] = self.value
            self.value += self.step
        return len(y)
