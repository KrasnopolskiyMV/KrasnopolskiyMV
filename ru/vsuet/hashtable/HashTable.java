package vsuet.hashtable;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


//public class HashTable<K, V> {
class HashTable<K, V> {
   private static final int DEFAULT_SIZE = 16;
   private List<Entry<K, V>>[] table = new List[16];
   private int size = 0;

   public HashTable() {
   }

   public void put(K key, V value) {
      int index = this.getIndex(key);
      List<Entry<K, V>> bucket = this.table[index];
      if (bucket == null) {
         bucket = new ArrayList();
         this.table[index] = (List)bucket;
      }

      Iterator var5 = ((List)bucket).iterator();

      Entry entry;
      do {
         if (!var5.hasNext()) {
            ((List)bucket).add(new Entry(key, value));
            ++this.size;
            return;
         }

         entry = (Entry)var5.next();
      } while(!entry.getKey().equals(key));

      entry.setValue(value);
   }

   public V get(K key) {
      int index = this.getIndex(key);
      List<Entry<K, V>> bucket = this.table[index];
      if (bucket != null) {
         Iterator var4 = bucket.iterator();

         while(var4.hasNext()) {
            Entry<K, V> entry = (Entry)var4.next();
            if (entry.getKey().equals(key)) {
               return entry.getValue();
            }
         }
      }

      return null;
   }

   public void remove(K key) {
      int index = this.getIndex(key);
      List<Entry<K, V>> bucket = this.table[index];
      if (bucket != null) {
         Iterator var4 = bucket.iterator();

         while(var4.hasNext()) {
            Entry<K, V> entry = (Entry)var4.next();
            if (entry.getKey().equals(key)) {
               bucket.remove(entry);
               --this.size;
               return;
            }
         }
      }

   }

   public boolean containsKey(K key) {
      int index = this.getIndex(key);
      List<Entry<K, V>> bucket = this.table[index];
      if (bucket != null) {
         Iterator var4 = bucket.iterator();

         while(var4.hasNext()) {
            Entry<K, V> entry = (Entry)var4.next();
            if (entry.getKey().equals(key)) {
               return true;
            }
         }
      }

      return false;
   }

   public int size() {
      return this.size;
   }

   private int getIndex(K key) {
      int hashCode = key.hashCode();
      return Math.abs(hashCode) % this.table.length;
   }
}