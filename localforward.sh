source vars.sh

ssh -p $SSH_PORT -N -f -L $LOCAL_PORT:localhost:$RELAY_PORT $RELAY_USER@$RELAY_IP