# Use an official OpenJDK image
FROM openjdk:21-jdk-slim


RUN apt-get update

RUN apt-get install -y wget

# Set working directory
WORKDIR /minecraft

#COPY server.jar .

# Accept EULA
RUN echo "eula=true" > eula.txt

# Download server.jar
RUN wget https://piston-data.mojang.com/v1/objects/95495a7f485eedd84ce928cef5e223b757d2f764/server.jar


# Expose Minecraft default port
EXPOSE 25565

# Allocate RAM and run the server
CMD ["java", "-Xmx4G", "-Xms4G", "-jar", "server.jar", "nogui"]
