import { useQuery } from "@tanstack/react-query";
import axios from "axios";

interface APIResponse {
  id: number;
  name: string;
  description: string;
}

const fetchData = async (): Promise<APIResponse[]> => {
  const { data } = await axios.get("http://localhost:8000/album_tracker/api/v1/album/");
  return data;
};

export function useFetchData() {
  return useQuery(['data',], async()=>{
                    const res = await fetchData;
                    return res;});
}
