# AI-on-FastAPI-with-Training

## Usage

### Running it local (not dockerized)

Install the requirements

```
pip install -r requirements.txt
```

Run the app

```
python main.py
```

### Running it local (dockerized)
Build the docker image 
```
 docker build -t ai_image . 
```
Run the docker container
```
docker run -p 8080:8080 ai_image 
```

### What happend after this?
Now you can look your AI up on the following localhost: [localhost:8080](localhost:8080)<br>
If it sends you a message, you are good to go.<br>
Now enter [localhost:8080/docs](localhost:8080/docs) <br>

In the first CRUD command you can use the AI and send some requests.
Settings are mentioned in the source code commented.

### Training
In the second CRUD command you can Upload a file which has to be a .txt. <br>
There is a certain pattern recommended to use while processing the training data.

```
User:  So the brain is adjusting a little bit. We don't know how much and the machine is adjusting. Where do you see as they try to reach together almost like with an alien species, try to find a protocol, communication protocol that works. Where do you see the biggest benefit arriving from, on the machine side or the human side? Do you see both of them working together?

Elon Musk:  I think the machine side is far more malleable than the biological side, by a huge amount. So it'll be the machine that adapts to the brain. That's the only thing that's possible. The brain can't adapt that well to the machine. You can't have neurons start to regard an electrode as another neuron. Because a neuron just, it's like the pulse and so something else is pulsing. See, so there is that elasticity in the interface, which we believe is something that can can happen, but the vast majority of the malleability will have to be on the machine side.

User: But it's interesting when you look at that synaptic plasticity at the interface side, there might be an emergent plasticity. Because it's whole nother, it's not like in the brain, it's a whole nother extension of the brain. We might have to redefine what it means to be malleable for the brain. So maybe the brain is able to adjust to external interfaces.

Elon Musk:  There'll be some adjustments to the brain because there's going to be something reading and simulating the brain, and so it will adjust to that thing. But the vast majority of the adjustment will be on the machine side. This is just, it has to be that, otherwise it will not work. Ultimately, we currently operate on two layers. We have a limbic like prime primitive brain layer, which is where all of our impulses are coming from. It's like we've got a monkey brain with a computer stuck on it, that's the human brain. And a lot of our impulses and everything are driven by the monkey brain, and the computer, the cortex is constantly trying to make the monkey brain happy. It's not the cortex that's steering the monkey brain, the monkey brain's steering the cortex.
```
Credits to [forefrontai.medium.com](https://forefrontai.medium.com/preparing-a-dataset-to-fine-tune-gpt-j-eafa2e66d6b4#:~:text=and%20customer%20issues.%E2%80%8D-,The%20dataset%20might%20look%20like%20the%20following%3A,-An%20optional%20improvement)
