# Added To Show Commit
# Thnks To @MrConfused
FROM starkgang/FridayUserbot:latest

#clone repo
RUN git clone https://github.com/StarkGang/FridayUserbot.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
