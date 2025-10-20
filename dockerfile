# Use an official OpenJDK image
FROM openjdk:21-jdk-slim

# Set working directory
WORKDIR /minecraft

COPY server.jar .

# Accept EULA
RUN echo "eula=true" > eula.txt

# Expose Minecraft default port
EXPOSE 25565

# Allocate RAM and run the server
CMD ["java", "-Xmx4G", "-Xms4G", "-jar", "server.jar", "nogui"]
