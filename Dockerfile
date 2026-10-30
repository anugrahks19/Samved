FROM maven:3.9.9-eclipse-temurin-17 AS build
WORKDIR /workspace
COPY backend/pom.xml backend/pom.xml
COPY backend/src backend/src
COPY ["SAMVED_Portal_Updated/JAVA PROJECT OOP", "SAMVED_Portal_Updated/JAVA PROJECT OOP"]
RUN mvn -B -f backend/pom.xml -DskipTests package

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /workspace/backend/target/samved-backend-0.1.0-SNAPSHOT.jar /app/samved.jar
EXPOSE 10000
ENTRYPOINT ["java", "-jar", "/app/samved.jar"]
