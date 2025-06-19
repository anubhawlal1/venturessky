import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

interface Restaurant {
  id: number;
  name: string;
  address: string;
  phone_number: string;
  rating: number;
}

const RestaurantDetail = ({ route }: any) => {
  const { restaurant } = route.params as { restaurant: Restaurant };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.name}>{restaurant.name}</Text>
        <View style={styles.infoContainer}>
          <Text style={styles.label}>Rating:</Text>
          <Text style={styles.value}>{restaurant.rating}/5</Text>
        </View>
        <View style={styles.infoContainer}>
          <Text style={styles.label}>Address:</Text>
          <Text style={styles.value}>{restaurant.address}</Text>
        </View>
        <View style={styles.infoContainer}>
          <Text style={styles.label}>Phone:</Text>
          <Text style={styles.value}>{restaurant.phone_number}</Text>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  card: {
    backgroundColor: '#f9f9f9',
    margin: 16,
    padding: 20,
    borderRadius: 8,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  name: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
    color: '#333',
  },
  infoContainer: {
    flexDirection: 'row',
    marginBottom: 12,
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#666',
    width: 80,
  },
  value: {
    fontSize: 16,
    color: '#333',
    flex: 1,
  },
});

export default RestaurantDetail; 