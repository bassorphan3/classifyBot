install.sh
cd .data
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
wget https://pjreddie.com/media/files/darknet19.weights
wget https://pjreddie.com/media/files/yolov3-tiny.weights
@bot.message_handler(content_types=['photo'])
def handle(message):
  # extract the image name for further operations
  image_name = save_image_from_message(message)
  
  # execute object recognition
  object_recognition_image(image_name)
  # send object recognition results
  bot.send_photo(message.chat.id, open('.data/darknet/predictions.jpg','rb'), 'Identified objects')
  
  # execute image classification
  classification_list_result = classify_image(image_name)
  
  # send classification results
  output = 'The image classifies as:\n'
  for result in classification_list_result:
    output += result
  output += '\nIngresa una imagen'
    
  bot.reply_to(message, output)
  
  # remove picture from server
  cleanup_remove_image(image_name);