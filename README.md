# multiprocessing-tensorflow
Run Tensorflow/Keras models in parallel with multiprocessing

Run the example script: 

```bash
python mptf.py
```

and you should see something like:

```
Worker 1 working...
Worker 2 working...
Worker 1 done!
Worker 3 working...
Worker 2 done!
Worker 4 working...
Worker 3 done!
Worker 5 working...
Worker 4 done!
Worker 5 done!
['Worker 1 OK!', 'Worker 2 OK!', 'Worker 3 OK!', 'Worker 4 OK!', 'Worker 5 OK!']
```

It seems that this workaround is not necessary anymore in Tensorflow 2.0.